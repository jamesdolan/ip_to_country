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
        self.time = time.perf_counter() - self.start
        if self.count > 1:
            self.readout = f'{self.name}: {self.time:.3f}s: {1000*self.time/self.count:.3f}ms per iteration'
        else:
            self.readout = f'{self.name}: {self.time:.3f}s'
        print(self.readout)

if __name__ == "__main__":
    rnd = random.Random(457475)
    with PerfScope("Load") as _:
        ctx = Context()
    test_count = 1000
    with PerfScope("Lookup", test_count) as _:
        for _ in range(test_count):
            ip = f"{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}.{rnd.randint(0,255)}"
            if cc := ctx.country_code(ip):
                print(cc)
            else:
                print("??")