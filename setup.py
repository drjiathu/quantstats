#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""QuantStats: Portfolio analytics for quants
https://github.com/drjiathu/quantstats
QuantStats performs portfolio profiling, to allow quants and
portfolio managers to understand their performance better,
by providing them with in-depth analytics and risk metrics.
"""

# This file is provided for backward compatibility.
# The project now uses pyproject.toml for modern Python packaging and dependency management.
# Please refer to pyproject.toml for the latest configuration.

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        # Basic metadata is now defined in pyproject.toml
        # This minimal setup.py ensures backward compatibility with tools that don't support pyproject.toml yet
        packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
        include_package_data=True,
    )
