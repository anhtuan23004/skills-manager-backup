#!/usr/bin/env node
/**
 * gen_deck_thumbs.mjs — Generate a thumbnail for each page of a multi-file deck (for the "infinite gallery" overview of deck_index.html).
 *
 * Background: deck_index.html has two overviews——
 *   · Grid (default, 60%): renders the real sub-pages with iframes; sharp and WYSIWYG, no thumbnails needed.
 *   · Infinite gallery (40%): tiles all pages seamlessly and infinitely + slow drifting; dozens to hundreds of tiles would lag if all were iframes,
 *     so the gallery uses <img> thumbnails instead——the same image reused many times is decoded only once by the browser, so it stays smooth.
 *   This script prepares those thumbnails for the gallery. Grid mode does not need it.
 *
 * Usage (copy to the deck project root, install dependencies, then run):
 *   npm install playwright sharp
 *   node gen_deck_thumbs.mjs --slides slides --out thumbs [--width 1600] [--quality 86]
 *
 * Then add a thumb to each entry in the MANIFEST in index.html (same name as file, .jpg):
 *   { file: "slides/01-cover.html", thumb: "thumbs/01-cover.jpg", label: "Cover" }
 * deck_index.html uses thumb only in gallery mode; grid mode always uses file (iframe). Without a thumb, the gallery falls back to an iframe.
 *
 * Tip: do not make the thumbnail resolution too low (default 1600px), or cards will look blurry when hover-enlarged in the gallery.
 */
import { chromium } from 'playwright';
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const arg = (n, d) => { const i = process.argv.indexOf('--' + n); return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : d; };
const slidesDir = arg('slides', 'slides');
const outDir = arg('out', 'thumbs');
const width = parseInt(arg('width', '1600'), 10);
const quality = parseInt(arg('quality', '86'), 10);
const W = parseInt(arg('canvas-w', '1920'), 10);
const H = parseInt(arg('canvas-h', '1080'), 10);

if (!fs.existsSync(slidesDir)) { console.error('slides directory not found: ' + slidesDir); process.exit(1); }
fs.mkdirSync(outDir, { recursive: true });
const files = fs.readdirSync(slidesDir).filter(f => f.endsWith('.html')).sort();
if (!files.length) { console.error('no .html files in the slides directory'); process.exit(1); }

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
let ok = 0;
for (const f of files) {
  const base = f.replace(/\.html$/, '');
  const out = path.join(outDir, base + '.jpg');
  try {
    await page.goto('file://' + path.resolve(slidesDir, f), { waitUntil: 'load' });
    await page.waitForTimeout(2800);                 // wait for webfont / image paint
    const buf = await page.screenshot({ type: 'png', clip: { x: 0, y: 0, width: W, height: H } });
    await sharp(buf).resize(width).jpeg({ quality }).toFile(out);
    ok++; console.log('[ok] ' + out);
  } catch (e) { console.error('[FAIL] ' + f + ': ' + e.message); }
}
await browser.close();
console.log(`\n=== ${ok}/${files.length} thumbnails → ${outDir}/ ===`);
console.log('In the MANIFEST of index.html, add to each entry thumb: "' + outDir + '/<same-name>.jpg" (only used in gallery mode)');
