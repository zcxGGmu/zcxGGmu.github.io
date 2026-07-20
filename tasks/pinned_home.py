from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable


_CARD_RE = re.compile(r'(?P<card>\s*<a href="[^"]+" class="a-block">.*?</a>\s*)', re.S)
_HREF_RE = re.compile(r'href="([^"]+)"')
_PINNED_RE = re.compile(r'post-item-pinned|pin-badge')


def _split_home_block(html: str):
    cards = [m for m in _CARD_RE.finditer(html)]
    if not cards:
        return None
    return cards[0].start(), cards[-1].end(), [m.group("card") for m in cards]


def _card_url(card: str) -> str | None:
    match = _HREF_RE.search(card)
    return match.group(1) if match else None


def is_pinned_card(card: str) -> bool:
    return bool(_PINNED_RE.search(card))


def _rebuild_home_block(html: str, start: int, end: int, cards: list[str]) -> str:
    body = "".join(cards)
    if body and not body.startswith("\n"):
        body = "\n" + body
    return html[:start] + body + html[end:]


def _cards_body(cards: list[str]) -> str:
    body = "".join(cards)
    if body and not body.startswith("\n"):
        body = "\n" + body
    return body


def reorder_home_cards_first(html: str) -> str:
    split = _split_home_block(html)
    if not split:
        return html
    start, end, cards = split
    reordered = [card for card in cards if is_pinned_card(card)] + [card for card in cards if not is_pinned_card(card)]
    if reordered == cards and html[start:end] == _cards_body(cards):
        return html
    return _rebuild_home_block(html, start, end, reordered)


def insert_home_card_after_pinned(html: str, card: str, url: str | None = None) -> str:
    normalized = reorder_home_cards_first(html)
    split = _split_home_block(normalized)
    if not split:
        return html

    start, end, cards = split
    target_url = url or _card_url(card)
    if target_url and any(_card_url(existing) == target_url for existing in cards):
        return normalized

    pinned_count = sum(1 for existing in cards if is_pinned_card(existing))
    next_cards = cards[:]
    next_cards.insert(pinned_count, card)
    return _rebuild_home_block(normalized, start, end, next_cards)


def update_home_file(path: Path, card: str, url: str | None = None) -> None:
    if not path.exists():
        return
    path.write_text(insert_home_card_after_pinned(path.read_text(encoding="utf-8"), card, url), encoding="utf-8")


def update_home_files(root: Path, rels: Iterable[str], card: str, url: str | None = None) -> None:
    for rel in rels:
        update_home_file(root / rel, card, url)
