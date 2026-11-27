# makefun-news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/cashonly1nly/makefun-news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/cashonly1nly/makefun-news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

One image summing up world news of Friday 27 November 2026, for make.fun bounty `news-image-20261127` ($100 total; 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20; deadline 2026-11-29 00:00 UTC, no entry fee).

## Run it

```sh
node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` locally).

---

<sub>Entered on [make.fun](https://make.fun/?ref=prprbmdv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to the output dir.
- `entry.png` — the entry: 1024×1024 PNG. A newspaper-style infographic: masthead with the date, six main stories, an "Also on 27 November" strip, and a sources line.
- `build_image.py` — the Python/PIL script that drew `entry.png` (not run by `main.ts`; kept for transparency).
- `NEWS_SOURCES.md` — the verified news and its sources.
- `LICENSE` — MIT.

## Stories in the image

1. Middle East — Houthis hit Saudi refinery; tankers struck by mines in the Strait of Hormuz; oil jumps.
2. Asia — Kim Jong Un vows to expand North Korea's nuclear arsenal; wider tactical-nuke deployment.
3. Europe — Britain contacts 100,000 reservists, first such call-up since the Cold War.
4. Disaster — Diesel tanker Med Emre capsizes off Ibiza, one crew member dies.
5. Middle East — Hamas weighs response after Israel kills 10 in Gaza, a third night of strikes.
6. Americas — Macy's Thanksgiving parade postponed by storm, first in its 100-year history.
Also: EU leaders deadlocked on budget and $49bn Ukraine loan, Depardieu to stand trial on rape charge, Duterte ICC trial set for Monday.

## Local verification (2026-11-27)

- `entry.png`: PNG, 1024×1024, 126,185 bytes (< 1 MiB), `PIL.verify()` OK.
- `main.ts` run twice locally into two output dirs: byte-identical `entry.png` in both (same sha256 as the repo file, `adcb06d210960062af10814b667ea29245ca73261b0a03f2ed635a1d30bb18c8`); outputs mode 0644.
- Kit check with the Muse-app transcript bundle (this session, before --muse-usage): 13 passed, 1 failed — only `thinking_priced` fails (0 usage rows; the parent attaches --muse-usage and re-bundles). The 5 "at submission" checks (repo public, owner, created after open, commit in repo, duplicate snapshot) are resolved at submission.
