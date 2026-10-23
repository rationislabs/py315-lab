# free-threading

Python 3.15's free-threaded build (3.15t) runs threads without the GIL, so a thread pool
spreads CPU-bound work across cores. The demo hashes eight large strings in a
`ThreadPoolExecutor` and checks that the results match a plain loop. `hashlib` comes in through
a [PEP 810](https://peps.python.org/pep-0810/) `lazy import`: it loads on first use, not at
startup.

```sh
uv run free-threading     # Python 3.15.0, GIL off: ['1120a819', ...]
uv run pytest             # GIL off, same digests as a loop, hashlib not loaded at import
```

`.python-version` asks for `3.15+freethreaded`; uv downloads it. With `PYTHON_GIL=1` the demo
refuses to run.
