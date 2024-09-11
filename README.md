# 🌎 ip_to_country
Rewrite of [IPToCC](https://github.com/roniemartinez/IPToCC) with an emphesis on performance (>10000x faster queries!) and memory reduction (98% less!), with no external dependencies and database thats updated nightly. Designed to be blazy fast on even the smallest VPS cloud instances.

[![CI](https://github.com/jamesdolan/ip_to_country/actions/workflows/ci.yml/badge.svg)](https://github.com/jamesdolan/ip_to_country/actions/workflows/ci.yml)
[![Update](https://github.com/jamesdolan/ip_to_country/actions/workflows/update.yml/badge.svg)](https://github.com/jamesdolan/ip_to_country/actions/workflows/update.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jamesdolan/IPToCC-Live/blob/master/LICENSE)

## Performance
Measured on M3 MacBook Air with Python 3.9.6
- Context creation: `ctx = ip_to_country.Context()` -> 0.0015s (vs IPToCC 5s)
- IP to Country Code: `cc = ctx.country_code(ip)` -> 0.0182ms (vs IPToCC 237.057ms)
- Memory consumption: ~5.5MB (vs IPToCC 359MB)

## Features
- [x] No external API call
- [x] No paid GeoIP service
- [x] Offline
- [x] Database updated nightly 

To learn about using IP addresses for geolocation, read the [Wikipedia article](https://en.wikipedia.org/wiki/Geolocation_software) to gain a basic understanding.

## Install
Install the latest version with the latest database...
```bash
pip install git+https://github.com/jamesdolan/ip_to_country.git@main
```

## Usage
```python
import ip_to_country
ctx = ip_to_country.Context()
cc = ctx.country_code("<IPv4/IPv6 address>")
```

## References
- [RIR Statistics Exchange Format](https://www.apnic.net/about-apnic/corporate-documents/documents/resource-guidelines/rir-statistics-exchange-format/)
- [How can I compile an IP address to country lookup database to make available for free?](https://webmasters.stackexchange.com/questions/34628/how-can-i-compile-an-ip-address-to-country-lookup-database-to-make-available-for)
- [ISO 3166 Country Codes](https://dev.maxmind.com/geoip/legacy/codes/iso3166/)