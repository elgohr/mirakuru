# Copyright (C) 2014 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).

# This file is part of mirakuru.

# mirakuru is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# mirakuru is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with mirakuru.  If not, see <http://www.gnu.org/licenses/>.
"""Mirakuru installation module."""

import os
from setuptools import setup, find_packages


here = os.path.dirname(__file__)


requirements = [
    # psutil is used to find processes leaked during termination.
    # It runs on many platforms but not Cygwin:
    # <https://github.com/giampaolo/psutil/issues/82>.
    'psutil>=4.0.0; sys_platform != "cygwin"',
]

tests_require = (
    'pytest',  # tests framework used
    'pytest-cov',  # coverage reports to verify tests quality
    'python-daemon',  # used in test for easy creation of daemons
)
extras_require = {
    'docs': ['sphinx'],
    'tests': tests_require,
}


def read(fname):
    """
    Read filename.

    :param str fname: name of a file to read
    """
    return open(os.path.join(here, fname)).read()


setup(
    name='mirakuru',
    version='2.2.0',
    description='Process executor for tests.',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
    ),
    keywords='process executor tests summon_process',
    url='https://github.com/ClearcodeHQ/mirakuru',
    author='Clearcode - The A Room',
    author_email='thearoom@clearcode.cc',
    license='LGPL',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    tests_require=tests_require,
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
)
