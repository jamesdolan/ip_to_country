#!/usr/bin/env python3

import random
import time

from ip_to_country import Context

class PerfScope:
    def __init__(self, name, count=1):
        self.name = name
        self.count = count

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        delta = time.perf_counter() - self.start
        self.readout = f'{self.name}: {delta:.4f}s'
        print(self.readout)

if __name__ == "__main__":
    rnd = random.Random(457475)
    with PerfScope("Load") as _:
        ctx = Context()
    with PerfScope("Lookup") as _:
        for _ in range(1000):
            ip = f"{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}"
            if cc := ctx.country_code(ip):
                print(cc)
            else:
                print("??")