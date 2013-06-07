#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='kegerface',
    version='0.1',
    description='Kegerface Django Application, based on the kegerface application at https://github.com/kegerface/kegerface',
    author='Jason Zylks',
    author_email='jzylks@gmail.com',
    license='Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License',
    url='https://github.com/jzylks/kegerface',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django'],
    zip_safe=False,
)
