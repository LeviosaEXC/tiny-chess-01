# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/LeviosaEXC/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/LeviosaEXC/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A deterministic chess engine in a single compressed Python payload (4,084 bytes). `main.py` is the kit-compress stub around an LZMA stream of the readable engine source: negamax with alpha-beta, a move-only transposition table, null-move pruning, late-move reductions, a capture quiescence search, tapered material + piece-square evaluation, and iterative deepening under a fixed 250,000-node cap per move — stdlib only, no clock, no unseeded randomness, so replays are byte-identical. It speaks the trial environment's HTTP protocol and plays legal UCI moves.

## License

MIT — see LICENSE.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x7rn5fey&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
