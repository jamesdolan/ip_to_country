#!/usr/bin/env python3

from setuptools import setup # type: ignore [import-untyped]

setup(
    name="ip_to_country",
    packages=[
        "ip_to_country",
    ],
    package_data={
        "ip_to_country": [
            "*.bin",
        ],
    },
    python_requires='>=3.9',
)
