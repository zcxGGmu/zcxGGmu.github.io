import fs from "node:fs";
import assert from "node:assert/strict";

const coverSvg = fs.readFileSync(
  new URL("../images/posts/inside-the-black-box-quant-investing-summary/quant-blackbox-cover.svg", import.meta.url),
  "utf8"
);

assert.doesNotMatch(
  coverSvg,
  />数据<|>订单</,
  "The in-article title card should not include external pipeline nodes"
);

