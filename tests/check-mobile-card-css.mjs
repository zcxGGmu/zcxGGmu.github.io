import fs from "node:fs";
import assert from "node:assert/strict";

const css = fs.readFileSync(new URL("../scss/modern.min.css", import.meta.url), "utf8");
const mediaBlocks = [...css.matchAll(/@media screen and \(max-width: 1020px\) \{([\s\S]*?)\n\}/g)];

assert.ok(mediaBlocks.length, "Expected a max-width: 1020px media query in modern.min.css");

const mobileCss = mediaBlocks.at(-1)[1];
const imageRuleMatch = mobileCss.match(
  /\.stream-container \.post-list-container \.post-item-wrapper \.post-item \.post-item-image-wrapper \.post-item-image\s*\{([^}]*)\}/
);

assert.ok(imageRuleMatch, "Expected a mobile post item image rule");
assert.match(
  imageRuleMatch[1],
  /width:\s*100%/,
  "Mobile post item images must fill the card width"
);
