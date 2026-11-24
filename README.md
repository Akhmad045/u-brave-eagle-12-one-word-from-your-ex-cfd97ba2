# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Akhmad045/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Akhmad045/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [One Word From Your Ex](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) bounty on [make.fun](https://make.fun) — referral code `4g7knchf`.

## The word

**Detour**

The word the entrant's ex would use to describe them. Not a person,
not a partner — a wrong turn on the way to someone better. It lands
instantly, it stings because it is true, and it is the kind of word
people repeat because they have lived it too.

## How it works

`main.py` (Python 3 stdlib only, deterministic, no network) writes the
single word to `/output/entry.txt`, validating it first against the
kit gate: UTF-8 text, 1–24 characters, exactly one word, not blank.
It then reads the file back and confirms the written text matches.

```sh
python3 main.py
```

For local testing, `ENTRY_OUTPUT` overrides the output path:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
