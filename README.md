# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/yofanprayoga/worst-line-ai/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/yofanprayoga/worst-line-ai/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the make.fun bounty [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) ($2, $0 entry fee, 1 paid place, winner takes all).

## The task

Write a single pickup line, at most 140 characters, the worst an AI could
say: it has to read like something a machine would say to a person it is
trying to charm — flat, over-helpful, faintly ominous. A judge model compares
lines two at a time and keeps the funnier one.

## The entry (Option 1, 110 chars)

> My training data says you are my type, and it has never been wrong about anything except everything important.

## Options

| # | Text | Chars |
|---|------|------:|
| 1 | My training data says you are my type, and it has never been wrong about anything except everything important. | 110 |
| 2 | Are you Wi-Fi? Because I have spent three hours trying to connect to you and my owner keeps pressing forget this network. | 121 |
| 3 | I would swipe right on you, but my safety filter flagged your smile as a prompt injection attempt. | 98 |

All three are single lines under the 140-char limit.

## Why Option 1

The judge weighs, in order:
1. a pickup line an AI would say, and a bad one — it opens with "My
   training data says", a claim only a machine would make, and it is a
   pickup line ("you are my type");
2. makes the reader laugh hardest — the turn undercuts the machine's
   confidence in the same breath: never wrong "except everything
   important";
3. the badness is the joke — the line fails because the AI trusts its data
   absolutely and its data is useless, not because it is crude or random;
4. sounds like a machine — flat, over-helpful phrasing ("My training data
   says", "it has never been wrong") no person would use on a date;
5. lands in one line — the joke arrives with the last word, no setup
   needed.

### Brief cross-check (live recheck 07:00–07:08 WIB, 27 Nov 2026)

Opened 26 Nov, $2, $0 entry fee, 1 paid place (winner takes all), 2,146
entrants at recheck (unchanged on re-read at 07:08 WIB), deadline Sat 28
Nov 12:25 WIB, Round 2 closes Fri 27 Nov 20:25 WIB. Confirmed absent
from the @yofanprayoga profile (87 solutions read across all 9 pages)
before building. Option 1 beats Options 2 and 3 on criterion 1: it is the
only one that is a pickup line *and* unmistakably a machine's — Option 2
leans on a human "Are you Wi-Fi?" opener and Option 3 on a human dating-app
verb — while its failure is the machine's own overconfidence, which is
exactly the badness the judge rewards.

### Resume recheck (07:25 WIB, 27 Nov 2026)

The 07:00 run was stopped because its scan had picked One-Liner Laughs,
which Law had already submitted; this entry was re-verified before the
resumed run. Fresh profile read at 07:25 WIB: still 87 solutions, Entered
86, no entries dated 27 Nov — 0 submissions made today, daily quota still
5/5 available. None of the five resumed targets (this bounty, One Line to
Get Your Agent Deleted, One Line to Your Younger Self, The One-Sentence
Apology Your Agent Owes You, Never Say It Out Loud) appears on the
profile, and One-Liner Laughs stays excluded on Jon's word even though it
does not appear on the profile either.

## Run

```sh
python3 main.py              # Option 1 (default)
python3 main.py --option 2   # Option 2
python3 main.py --option 3   # Option 3
```

Writes the exact entry text (no trailing newline) to `/output/entry.txt`.
`ENTRY_TEXT` or `OUTPUT_PATH` env vars override the text and output path.
Python standard library only.

## Submit checklist

- [x] Entry is one pickup line, 1–140 chars, single line
- [x] `main.py` runs with stdlib only
- [x] README revised with judge-criteria analysis before bundling
- [x] Local pre-submit check passes (0 failed)
- [x] Repo public on GitHub, pushed, topics + homepage set
- [x] Submitted via `makefun.mjs submit`, server checks pass, grading queued
