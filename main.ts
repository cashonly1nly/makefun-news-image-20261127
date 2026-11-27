// news-image-20261127 entry (Node 22, standard library only).
// The image is entry.png beside this file, drawn by build_image.py from
// verified 27 November 2026 news (see NEWS_SOURCES.md). The program copies
// it to /output/entry.png, exactly as the kit's starter does.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const src = new URL('./entry.png', import.meta.url);
if (!existsSync(src) || statSync(src).size === 0) {
  console.error('error: entry.png is missing or empty next to main.ts');
  process.exit(1);
}

const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(out, { recursive: true });
copyFileSync(src, join(out, 'entry.png'));
