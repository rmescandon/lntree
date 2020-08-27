#!/usr/bin/env python3
#
# Copyright (C) 2020 Roberto Mier Escandon <rmescandon@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import setuptools

with open('requirements.txt') as f:
    install_requirements = f.read().strip().split('\n')

setuptools.setup(
    name="lntree",
    version='0.1.0',
    author="Roberto Mier Escandon",
    author_email="rmescandon@gmail.com",
    description="A simple tool to symlink the leaves of a directory tree to a certain folder(s) or file(s)",
    url="https://github.com/telefonicaid/lntree",
    install_requires=install_requirements,
    packages=setuptools.find_packages(),
    platforms='linux',
    entry_points={'console_scripts': ['lntree=lntree.lntree:link_tree']},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux'
    ],
)
