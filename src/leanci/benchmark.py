
import time

import httpx


def measure_request(url: str) -> float:
    start = time.perf_counter()

    response = httpx.get(url, timeout=10.0)
    response.raise_for_status()

    elapsed = time.perf_counter() - start
    return elapsed
