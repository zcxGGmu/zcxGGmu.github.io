# Blog Card Layout Fix

- [x] Add a regression check for mobile post card cover width.
- [x] Verify the regression check fails on the current CSS.
- [x] Fix the mobile post card image rule in `scss/modern.min.css`.
- [x] Run build and automated verification.
- [x] Inspect the homepage at 901px width.
- [x] Record review notes.
- [x] Commit and push to `origin/gh-pages`.

## Review

- Root cause: `modern.min.css` loaded after `journal.min.css` and reset `.post-item-image` to `width: 220px`; the later mobile override only changed height and border radius.
- Fix: set mobile `.post-item-image` to `width: 100%` inside the existing `max-width: 1020px` rule.
- Verification: `node tests/check-mobile-card-css.mjs`, `npm run build`, and a 901x857 Chromium screenshot of `http://127.0.0.1:4173/`.

# Quant Black Box Cover Fix

- [x] Add a regression check for the article featured image.
- [x] Verify the regression check fails on the current post.
- [x] Add a title-free hero image for the article page.
- [x] Keep the existing title card as the first in-article image.
- [x] Run build and automated verification.
- [x] Inspect the article page at desktop width.
- [x] Record review notes.
- [x] Commit and push to `origin/gh-pages`.

## Review

- Root cause: the post `featured_image` reused the in-article title card SVG, while the article template overlays title, description, date, tags, and reading time on top of featured images.
- Fix: add `quant-blackbox-hero.svg` as a title-free decorative hero image and point the post front matter at it. The original title card remains as the first image in the article body.
- Verification: `node tests/check-quant-blackbox-featured-image.mjs`, `node tests/check-mobile-card-css.mjs`, `npm run build`, and a 1200x900 Chromium screenshot of the article page.
