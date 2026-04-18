#!/usr/bin/env python3

import os
from array import array

from ip_to_country import IPV4_PATH, IPV4_TYPECODE

if __name__ == "__main__":
    with open(IPV4_PATH, "rb") as f:
        f_size = os.fstat(f.fileno()).st_size
        count = f_size // 6
        assert count * 6 == f_size
        ipv4_start = array(IPV4_TYPECODE)
        ipv4_start.fromfile(f, count)
        ipv4_cc = f.read(count * 2).decode("ascii")

    merged_start = array(IPV4_TYPECODE)
    merged_cc: list[str] = []
    for i in range(count):
        cc = ipv4_cc[i*2:i*2+2]
        if merged_cc and merged_cc[-1] == cc:
            continue
        merged_start.append(ipv4_start[i])
        merged_cc.append(cc)

    merged_count = len(merged_start)
    print(f"Entries: {count} -> {merged_count} ({count - merged_count} merged)")
    print(f"Size: {f_size} -> {merged_count * 6} bytes")

    with open(IPV4_PATH, "wb") as f:
        f.write(merged_start.tobytes())
        f.write("".join(merged_cc).encode("ascii"))
