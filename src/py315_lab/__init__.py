import sys
from concurrent.futures import ThreadPoolExecutor

lazy import hashlib  # PEP 810: loaded on first use, not at startup


def work(n: int) -> str:
    return hashlib.sha256(str(n).encode() * 100_000).hexdigest()[:8]


def main() -> None:
    gil = sys._is_gil_enabled()
    with ThreadPoolExecutor() as pool:
        digests = list(pool.map(work, range(8)))
    print(f"Python {sys.version.split()[0]}, GIL {'on' if gil else 'off'}: {digests}")
    assert not gil, "expected the free-threaded build (3.15t)"
