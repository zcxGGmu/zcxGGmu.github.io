import fs from "node:fs/promises";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");
const port = Number(process.env.PORT || process.argv[2] || 4173);

const types = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8"
};

function resolveRequest(url) {
  const parsed = new URL(url, "http://localhost");
  const decoded = decodeURIComponent(parsed.pathname);
  const clean = decoded.replace(/^\/+/, "");
  let target = path.join(rootDir, clean);
  if (!target.startsWith(rootDir)) return null;
  return target;
}

async function fileForRequest(url) {
  const target = resolveRequest(url);
  if (!target) return null;
  try {
    const stat = await fs.stat(target);
    if (stat.isDirectory()) return path.join(target, "index.html");
    return target;
  } catch {
    return path.join(target, "index.html");
  }
}

const server = http.createServer(async (req, res) => {
  try {
    const file = await fileForRequest(req.url || "/");
    if (!file || !file.startsWith(rootDir)) {
      res.writeHead(403);
      res.end("Forbidden");
      return;
    }
    const data = await fs.readFile(file);
    res.writeHead(200, {
      "Content-Type": types[path.extname(file)] || "application/octet-stream",
      "Cache-Control": "no-store"
    });
    res.end(data);
  } catch {
    const fallback = path.join(rootDir, "404.html");
    try {
      const data = await fs.readFile(fallback);
      res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
      res.end(data);
    } catch {
      res.writeHead(404);
      res.end("Not found");
    }
  }
});

server.listen(port, "127.0.0.1", () => {
  console.log(`Serving ${rootDir} at http://127.0.0.1:${port}/`);
});
