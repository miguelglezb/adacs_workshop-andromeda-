#! /usr/bin/env python
"""
Set up for mymodule
"""

from setuptools import setup
import os

requirements = ['numpy>=1.0']


setup(
    name='mymodule',
    version=0.1,
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts':['sky_sim= mymodule.sky_sim:main']}
)
