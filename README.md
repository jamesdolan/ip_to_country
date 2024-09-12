# 🌎 ip_to_country
Rewrite of [IPToCC](https://github.com/roniemartinez/IPToCC) with an emphesis on performance (>10000x faster queries!) and memory reduction (99% less!), with no external dependencies and database that is updated nightly. Designed to be blazing fast on even the smallest VPS cloud instances.

[![CI](https://github.com/jamesdolan/ip_to_country/actions/workflows/ci.yml/badge.svg)](https://github.com/jamesdolan/ip_to_country/actions/workflows/ci.yml)
[![Update](https://github.com/jamesdolan/ip_to_country/actions/workflows/update.yml/badge.svg)](https://github.com/jamesdolan/ip_to_country/actions/workflows/update.yml)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jamesdolan/ip_to_country/blob/master/LICENSE)

## Features
- [x] No external API call
- [x] No paid GeoIP service
- [x] Offline
- [x] Database updated nightly 
- [x] IPv4
- [ ] IPv6 (TODO)

## Performance
Measured on M3 MacBook Air with Python 3.9.6
- Load database: `ctx = ip_to_country.Context()` -> 0.0006s (vs IPToCC 19.158s)
- IP to Country Code: `cc = ctx.country_code(ip)` -> 0.0182ms (vs IPToCC 237.057ms)
- Peak memory consumption: ~3MB (vs IPToCC 394MB)

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
- [Wikipedia article](https://en.wikipedia.org/wiki/Geolocation_software)
- [RIR Statistics Exchange Format](https://www.apnic.net/about-apnic/corporate-documents/documents/resource-guidelines/rir-statistics-exchange-format/)
- [ISO 3166 Country Codes](https://dev.maxmind.com/geoip/legacy/codes/iso3166/)
