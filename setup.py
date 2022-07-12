from setuptools import setup, find_packages
import sys
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = sys.version_info[:2]
if version < (3, 9):
    print('resources requires Python version 3.9 or later' +
          ' ({}.{}) detected.'.format(*version))
    sys.exit(-1)

VERSION = '0.1.0'

install_requires = ['click']

setup(name='resources',
      version=VERSION,
      py_modules=['pytodo'],
      description='A CLI tool for managing todo lists ',
      long_description=long_description,
      author='Caleb Farrell',
      author_email='caleb.farrell987@gmail.com',
      url='https://github.com/cfarrell987/pyTodo',
      license='GPLv3',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      entry_points={'console_scripts': ['pytd = src.pyTodo.main:pytd']})
