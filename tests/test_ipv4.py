#!/usr/bin/env python3

import pytest
import random

from ip_to_country import Context

def test_country_code():
    ctx = Context()
    assert ctx.country_code("8.8.8.8")    == "US"
    assert ctx.country_code("5.35.192.0") == "US"
    assert ctx.country_code("5.35.184.0") == "SE"


def test_ipv4_private():
    ctx = Context()
    assert ctx.country_code("10.0.0.0") == None
    assert ctx.country_code("0.0.0.0") == None
    assert ctx.country_code("127.0.0.1") == None
    assert ctx.country_code("172.16.0.0") == None
    assert ctx.country_code("255.255.255.255") == None


def test_invalid_ip():
    ctx = Context()
    with pytest.raises(ValueError):
        ctx.country_code("123456")

def test_stress():
    rng = random.Random(1)
    ctx = Context()
    for _ in range(1000):
        ip = f"{rng.randint(0,255)}.{rng.randint(0,255)}.{rng.randint(0,255)}.{rng.randint(0,255)}"
        cc = ctx.country_code(ip)
        assert not cc or len(cc) == 2
