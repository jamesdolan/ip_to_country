#!/usr/bin/env python3

import array
import bisect
import os
import struct
from ipaddress import IPv4Address
from typing import Union

PACKAGE_DIR   = os.path.dirname(os.path.abspath(__file__))
IPV4_PATH     = os.path.join(PACKAGE_DIR, "ipv4.bin")
IPV4_TYPECODE = "I" if struct.calcsize("I") == 4 else "L"
assert struct.calcsize(IPV4_TYPECODE) == 4

class Context:
    def __init__(self):
        with open(IPV4_PATH, "rb") as f:
            f_size = os.fstat(f.fileno()).st_size
            count = f_size // 10
            assert count * 10 == f_size
            self.ipv4_start = array.array(IPV4_TYPECODE)
            self.ipv4_end = array.array(IPV4_TYPECODE)
            self.ipv4_start.fromfile(f, count)
            self.ipv4_end.fromfile(f, count)
            self.ipv4_cc = f.read(count*2).decode("ascii")
            assert len(self.ipv4_start) == count
            assert len(self.ipv4_end) == count
            assert len(self.ipv4_cc) == count * 2
    
    def country_code_v4(self, address: IPv4Address, default_value: Union[str,None] = None) -> Union[str, None]:
        assert isinstance(address, IPv4Address)
        addr = int(address)
        next = bisect.bisect_right(self.ipv4_start, addr)
        prev = next-1
        if not next or self.ipv4_end[prev] <= addr:
            return default_value
        return self.ipv4_cc[prev*2:prev*2+2]

    def country_code(self, address: str, default_value: Union[str,None] = None) -> Union[str, None]:
        return self.country_code_v4(IPv4Address(address), default_value)