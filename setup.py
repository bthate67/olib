# This file is place in the Public Domain.

from setuptools import setup, os

def read():
    return open("README.rst", "r").read()

setup(
    name='olib',
    version='103',
    description="python3 object library",
    author='Bart Thate',
    author_email='bthate67@gmail.com', 
    url='https://github.com/bthate67/olib',
    long_description=read(),
    license='Public Domain',
    packages=["ol"],
    zip_safe=True,
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
