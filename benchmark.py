#!/usr/bin/env python3

import random
import time
import tracemalloc

from ip_to_country import Context

class PerfScope:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        delta = time.perf_counter() - self.start
        print(f'{self.name}: {delta:.4f}s')

if __name__ == "__main__":
    rnd = random.Random(457475)
    tracemalloc.start()
    with PerfScope("Load Context") as _:
        ctx = Context()
    with PerfScope("1000x Lookups") as _:
        for _ in range(1000):
            ip = f"{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}"
            ctx.country_code(ip)
    _, peak_memory = tracemalloc.get_traced_memory()
    print(f"Peak memory usage: {peak_memory}")