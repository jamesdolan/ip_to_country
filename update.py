import os
from array import array
from ipaddress import IPv4Address
from multiprocessing import Pool
from urllib.request import urlopen

from ip_to_country import IPV4_PATH

SOURCE_URLS = [
    "https://ftp.afrinic.net/stats/afrinic/delegated-afrinic-extended-latest",
    "https://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest",
    "https://ftp.apnic.net/public/apnic/stats/apnic/delegated-apnic-extended-latest",
    "https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest",
    "https://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest",
]

def download_file(url: str) -> str:
    print(f"Downloading {url}...")
    with urlopen(url) as response:
        data = response.read().decode("utf-8")
    print(f"Parsing {url}...")
    rows = [
        [col.strip() for col in line.split("|")]
        for line in data.splitlines()
        if not line.startswith('#')
    ]
    ipv4_rows = [
        [int(IPv4Address(start)),int(value),cc]
        for _,cc,type,start,value,*_ in rows
        if type == "ipv4" and len(cc) == 2
    ]
    return ipv4_rows

if __name__ == "__main__":
    with Pool() as pool:
        ipv4_srcs = pool.map(download_file, SOURCE_URLS)
    ipv4_rows = sorted(
        [
            row
            for src in ipv4_srcs
            for row in src
        ],
        key=lambda x: x[0]
    )
    ipv4_start = array("I", [
        int(start)
        for start,_,_ in ipv4_rows
    ])
    ipv4_counts = array("I", [
        int(count)
        for _,count,_ in ipv4_rows
    ])
    ipv4_cc = "".join([
        cc
        for _,_,cc in ipv4_rows
    ])
    with open(IPV4_PATH, "wb") as f:
        f.write(ipv4_start.tobytes())
        f.write(ipv4_counts.tobytes())
        f.write(ipv4_cc.encode("ascii"))