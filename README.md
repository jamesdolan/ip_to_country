# ip_to_country
Rewrite of [https://github.com/jamesdolan/IPToCC-Live](IPToCC) with an emphesis on performance (~22000x faster!) and memory reduction (98% less!).

Get ISO country code of IPv4/IPv6 address. Address lookup is done locally.

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jamesdolan/IPToCC-Live/blob/master/LICENSE)

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