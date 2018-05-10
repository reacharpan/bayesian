
# coding: utf-8

"""
Setup script for installing the project
"""

##########################################################################
## Imports
##########################################################################

from setuptools import setup, find_packages

##########################################################################
## Installation requirements
##########################################################################
install_requires = [
    "pymc3",
    "numpy"
]

##########################################################################
## Setup
##########################################################################

setup(
    name = "bayesian",
    packages = find_packages(),
    version = 0.1.0,
    description = "Lib to demonstrate bayesian methods",
    author = "Arpan P. Shah",
    license = "Apache License 2.0",
    url = "https://github.com/reacharpan/bayesian",
    install_requires = install_requires,
    keywords = ['pymc3', 'bayesian modelling'],
    classifiers = ['Programming Language :: Python', 'Programming Language :: Python :: 3.6']
)
