# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='Smart-Dispatch',
    version='0.0.2',
    author='Stanislas Lauly, Marc-Alexandre Côté, Mathieu Germain',
    author_email='smart-udes-dev@googlegroups.com',
    packages=['smartDispatch'],
    scripts=['scripts/smartDispatch.py'],
    url='https://github.com/SMART-Lab/smartDispatch',
    license='LICENSE.txt',
    description='A batch job launcher for the Mammouth supercomputer.',
    long_description=open('README.txt').read(),
    install_requires=[]
)
