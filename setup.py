# coding: utf-8
import os
import glob
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages

setup(
    name='app',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        "app": ["models/*"],#DL model
    }
)

