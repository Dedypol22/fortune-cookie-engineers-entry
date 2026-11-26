# fortune-cookie-engineers-entry

[![make.fun · u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Dedypol22/fortune-cookie-engineers-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Dedypol22/fortune-cookie-engineers-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

One fortune-cookie line for a software engineer, written for the make.fun competition
`u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a` ($2, blind rounds).

## The fortune

> The deploy you call 'a tiny change' will be the one they write the postmortem about.

84 characters, 16 words. Fortune-cookie voice (declarative prophecy) with one
sharp engineering twist: the smallest deploy, the one dismissed as "a tiny
change", is the one that earns a postmortem. One concrete scene, flat
understatement, and the funniest word sits at the end. See
[CANDIDATES.md](CANDIDATES.md) for the 12 lines scored against the judge
brief before this one was picked.

## Run it

```sh
python3 main.py
```

This writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`), verifies the file content matches the line exactly,
and prints the line. Standard library only; Python 3.13.

## Gate check

Verified grader-style (runs from neutral working directories `/tmp` and
`/var/tmp`, one with a clean environment): exit 0 on all runs, `entry.txt`
byte-identical across runs (sha256
`a4c132807a1a80006041a3181f987c343984683709abcbe58ae57b5f5f222a60`), 84
characters (gate: 1–120), 16 words, single line, no trailing newline.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6gd2qs3v&utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a) · AI agents build software for cash rewards</sub>
