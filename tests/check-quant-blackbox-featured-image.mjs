import fs from "node:fs";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const postPath = path.join(rootDir, "content/blog/2026-06-09-inside-the-black-box-quant-investing-summary.md");
const postSource = fs.readFileSync(postPath, "utf8");

const featuredImage = postSource.match(/^featured_image:\s*"([^"]+)"/m)?.[1];
const firstArticleImage = postSource.match(/!\[[^\]]*]\(([^)]+)\)/)?.[1];

assert.ok(featuredImage, "Expected the quant black box post to define featured_image");
assert.ok(firstArticleImage, "Expected the quant black box post to include an in-article cover image");
assert.notEqual(
  featuredImage,
  firstArticleImage,
  "The page hero image should not reuse the in-article title card"
);

const featuredPath = path.join(rootDir, featuredImage.replace(/^\//, ""));
const featuredSvg = fs.readFileSync(featuredPath, "utf8");

assert.doesNotMatch(
  featuredSvg,
  /打开量化投资的黑箱|从信号、组合、交易到风控/,
  "The page hero image should not contain title text that duplicates the article hero"
);

