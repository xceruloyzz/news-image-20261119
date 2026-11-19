# The World Today — Thursday 19 November 2026 in One Image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/xceruloyzz/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/xceruloyzz/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One 1024×1024 PNG, drawn like a newspaper front page, that sums up Thursday 19 November 2026.

## The stories on the page

- **Lead — Grand Theft Auto VI launches.** The rollout begins at midnight local time, starting in New Zealand, after a 13-year wait. PlayStation 5 and Xbox Series X|S; close to 16 million preorders worth over $1.5bn; a Metacritic score of 99. (Reuters via TBS News; NorthJersey; Polygon, 18 Nov.)
- **US politics — Jeffries nominated for Speaker.** House Democrats pick Hakeem Jeffries 251–11; a floor vote on 3 January would make him the first Black Speaker. (NPR / Reuters, 18 Nov.)
- **Gulf escalation — Iran widens its attacks.** Tehran strikes a US air base in Kuwait and hits Bahrain again; a Houthi missile aimed at Riyadh is destroyed. (AP via Military.com; Reuters, 18 Nov.)
- **Diplomacy — Trump, Xi and Putin meet in Shenzhen.** The first trilateral of the three leaders, on the APEC sidelines: nuclear arms, Ukraine and Iran, for one hour. (Reuters, 18 Nov.)
- **Ukraine aid — EU proposes a €45bn loan.** Kyiv would repay only once Russia pays reparations; the loan covers two-thirds of a €70bn gap for 2027. (Reuters, 18 Nov.)
- **Weather — Cyclone Akvan nears India.** The severe storm is forecast to cross between Machilipatnam and Puri by noon on 20 November at 90–100 km/h, under a red alert. (IMD National Bulletin No. 27, 02:30 IST 19 Nov.)
- **Space — Voyager 1 is one light-day away.** The first human-made object a light-day from Earth, about 16 billion miles out; NASA briefs the milestone at noon EST today. (NASA; Popular Science, 18 Nov.)
- **Ticker** — PM Modi meets the Prince and Princess of Wales; Australia sanctions Israeli settlers; Democrat Peltola wins the Alaska Senate seat; Pew finds Islam on track to be the world's largest religion by 2035; Ben Duckett's 133 as England beat Australia.

## How it works

`main.py` (Python 3.13, standard library only) copies the committed `entry.png` beside it to the grading output location: `$MAKEFUN_OUTPUT_DIR/entry.png` if set, else `/output/entry.png` when `/output` exists, else `./out/entry.png`. It refuses to run if `entry.png` is missing. The picture itself is drawn by `tools/generate_frontpage.py`, a PIL renderer with every word hardcoded — no network, no randomness, no clock — so running it twice reproduces `entry.png` byte for byte. The renderer also asserts each headline wraps to at most two lines and each story body to at most three, so an over-long story fails loudly instead of overflowing the grid.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=ztsmgxnm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
