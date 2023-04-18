#!/usr/bin/env python
from setuptools import setup, find_packages



setup(
    extras_require={
        "dev": [
        ]
    },
    install_requires=[
    ],
    dependency_links=[], 
    license="Apache License 2.0",
    name="myhook",
    version="1.0.0",
    python_requires=">=3.7",
    description="Infrastructure as code static analysis",
    author="amansakhuja",
    author_email="aman.sakhuja21@gmail.com",
    packages=find_packages(exclude=["tests*", "integration_tests*"]),
    url="https://www.python.org/sigs/distutils-sig/",
    scripts=["bin/myhook"],
)
