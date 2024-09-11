#!/usr/bin/env python3

import array
import bisect
import os
from ipaddress import ip_address
from typing import Union

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
IPV4_PATH   = os.path.join(PACKAGE_DIR, "ipv4.bin")

class Context:
    def __init__(self):
        with open(IPV4_PATH, "rb") as f:
            data = f.read()
        count = len(data) // 10
        assert count * 10 == len(data)
        self.ipv4_start = array.array("I")
        self.ipv4_end = array.array("I")
        self.ipv4_start.frombytes(data[:count*4])
        self.ipv4_end.frombytes(data[count*4:count*8])
        self.ipv4_cc = data[count*8:].decode("ascii")
        assert len(self.ipv4_start) == count
        assert len(self.ipv4_end) == count
        assert len(self.ipv4_cc) == count * 2
    
    def country_code(self, addr_str: str) -> Union[str, None]:
        addr = int(ip_address(addr_str))
        next = bisect.bisect_right(self.ipv4_start, addr)
        prev = next-1
        if not next or self.ipv4_end[prev] <= addr:
            return None
        return self.ipv4_cc[prev*2:prev*2+2]