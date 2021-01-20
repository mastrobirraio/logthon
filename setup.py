from __future__ import with_statement

import os

NAME = 'logthon'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages


def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as fp:
        return fp.read()


requirements = [
    'colorama',
]

test_requirements = {
    'dev': [
        'coveralls',
        'freezegun',
    ] + requirements
}

setup(
    name=NAME,
    version='2.3.0',
    author='Giuseppe "mastrobirraio" Matranga',
    author_email='matrangagiuseppe99@gmail.com',
    maintainer='Giuseppe "mastrobirraio" Matranga',
    license='GPLv3',
    description='A simple logger for Python',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/mastrobirraio/logthon',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',
    ],
    install_requires=requirements,
    keywords='log logger logging logthon ansi crossplatform xplatform',
    python_requires='>=2.7',
)
