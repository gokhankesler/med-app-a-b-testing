#!/usr/bin/env python
#from distutils.core import setup
import re
from setuptools import setup, find_packages


setup(name='Med App A/B Testing',
      version='0.1.0',
      description='''This project implements A/B testing of a mobile app that offers 
      meditation services  for a paid subscription as well as one-off in-app purchases''',
      license="MIT",
      author='Gokhan Kesler',
      author_email='gokhankesler@gmail.com',
      packages=find_packages(include=["src", "src/*"]),
     )