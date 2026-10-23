import sys

import free_threading as ft


def test_runs_without_the_gil():
    # .python-version picks 3.15t; a regular build would make the thread pool a queue.
    assert not sys._is_gil_enabled()


def test_threads_give_the_same_digests_as_one_after_another():
    with ft.ThreadPoolExecutor() as pool:
        assert list(pool.map(ft.work, range(8))) == [ft.work(n) for n in range(8)]


def test_hashlib_is_imported_lazily():
    # PEP 810: the module is bound to a proxy until first use.
    import subprocess

    out = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys, free_threading; print('hashlib' in sys.modules)",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert out.stdout.strip() == "False"
