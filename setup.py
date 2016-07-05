#!/usr/bin/env python

from distutils.core import setup
import sys

if sys.version_info < (3,):
    package_dir = {'': 'code'}
else:
    package_dir = {'': 'code-python3'}


setup(name='data_science_from_scratch',
      version='1.1',
      description='Code examples of data science from the book Data Science From Scratch: First Principles with Python by Joel Grus',
      package_dir=package_dir,
     )
