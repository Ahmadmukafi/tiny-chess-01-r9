# tiny-chess-01-r9

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Ahmadmukafi/tiny-chess-01-r9/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Ahmadmukafi/tiny-chess-01-r9/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Round 9 of the 4KB Python chess engine for make.fun's tiny-chess-01 ($500). Deterministic fixed-node search with null-move pruning and a transposition table (ordering-only), in 4,075 bytes — under the 4,096-byte limit.

## Result

Trial-0 Elo **1,253** (1W / 4D / 3L) — above round 3's floor of 1,154. Mean across 3 trials: 1,138 (989, 1,173). The engine restores the transposition table cut and fixes the real bug found in round 8 (the move list was sorted in place while the UCI list was indexed by the sorted position, so the engine sometimes sent the wrong move).

## Files

- `main.py` — the engine (4,075 bytes, Python 3 stdlib only)
- `run_trial.sh` — the Elo harness (same trials as rounds 4–8)

---

<sub>Entered on [make.fun](https://make.fun/?ref=6z0bn4hz&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
