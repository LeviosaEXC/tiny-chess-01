# tiny-chess-01 entry

A deterministic chess engine in a single compressed Python payload.

`main.py` is a wrapper: `lzma` + `base64` around the readable engine
source. It decompresses and executes the engine at startup (stdlib only,
no network, no clock, no randomness). The engine is negamax with
alpha-beta, a transposition table, killer-move and MVV-LVA ordering, a
capture quiescence search, material + piece-square evaluation, and
iterative deepening under a fixed 50,000-node cap per move, so replays
are byte-identical. It speaks the trial environment's HTTP protocol
(`GET /game`, `POST /move`) and plays legal UCI moves.

Build: `lzma.compress(source, preset=9)`, base64-encoded into the
one-line wrapper. The wrapper is 3,856 bytes, under the 4,096-byte
entrypoint limit; the whole snapshot is under 8,192 bytes.

## License

MIT — see LICENSE.
