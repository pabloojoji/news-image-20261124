[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/pabloojoji/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/pabloojoji/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

[Enter this bounty on make.fun](https://make.fun/bounty/news-image-20261124)

# THE WORLD TODAY — 24 November 2026

Entry for make.fun bounty **news-image-20261124** — “Sum up 24 November's world news in one image”.

- Bounty: https://make.fun/bounty/news-image-20261124
- Deadline: Thu 26 Nov 2026, 07:00 WIB
- Prize (live table): $100 total, 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20, USDC on Solana
- Author: sgn88 (@sgn-8 on make.fun)

## How to run

Python 3.13, Pillow only. No network.

```bash
python3 main.py
# writes /output/entry.png (and ./output/entry.png)
```

## Output

- One whole PNG, **1024×1024, 107 KB** (limit: 1 MiB)
- Deterministic: same bytes on every run. Verified SHA256:
  `532b06f1bc5c89564fbf0a9ead09433d4d06bde1dcb04ef8ac9d2d7beb2ee417`
  Run twice, same hash.
- No `random`, no `Date.now()`, no network calls, no external images or fonts at render time (fonts are system DejaVu, bundled in the runner image).

## What is in the image

9 stories, all verified for 24 November 2026 only, with CONFIRMED / REPORTED / CLAIM tags and publisher + date:

1. COP31 ends with no deal on its main text — REPORTED, Carbon Brief / WRI, 24 Nov
2. Three tankers claimed hit by mines in Hormuz — CLAIM, IRNA / TBS, 24 Nov
3. Russian drone briefly enters Poland — CONFIRMED, Reuters, 24 Nov
4. Ukraine defends Libya ship strike — CONFIRMED, Reuters / CNN, 24 Nov
5. Nvidia brings back Jensen Huang — REPORTED, Reuters / CNN, 24 Nov
6. Fourteen nations back Myanmar genocide ruling — CONFIRMED, AFP, 24 Nov
7. Two US states sue over Grok images — CONFIRMED, AP / Reuters, 24 Nov
8. 5.6 quake shakes eastern Nepal — CONFIRMED, Nepal National Earthquake Centre, 24 Nov
9. Russia warns Estonia; satellite claim denied — REPORTED, Reuters, 23 Nov

Left out on purpose, shown in the image: US measles elimination status (announced 17 Nov, not 24 Nov); ICJ ruling itself (19 Nov).

Full sources with URLs: see `SOURCES.md`.
