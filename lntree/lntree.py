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


import click
import os

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def normalize(path):
    '''Expands user, vars and normalizes a path'''
    return os.path.expanduser(os.path.expandvars(os.path.normpath(path)))


def _split_and_map(paths):
    '''returns the a map with tail as key and head as value'''
    m = {}
    for p in paths:
        head, tail = os.path.split(p)

        if tail == '.':
            continue
        if tail == '..':
            continue
        if tail == '*':
            continue

        m[tail] = head
    return m


def _is_leaf(subfolders, ids):
    '''Returns true if there are no children other than the
    included in ids amongst subfolders'''
    for s in subfolders:
        if s not in ids:
            return False
    return True


def _ids_linked(subfolders, ids):
    '''Returns the list of sources in subfolders'''
    for i in ids:
        if i in subfolders:
            yield i


def _ids_not_linked(subfolders, ids):
    '''Returns the list of sources not in subfolders'''
    for i in ids:
        if i not in subfolders:
            yield i


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('src', nargs=-1)
@click.argument('dst')
@click.option('--clear/--no-clear', default=False)
def link_tree(src, dst, clear):
    '''
    Creates symlinks in all leaves in the dst tree to the src.

    \b
    SRC can be a file, a dir or a group of them (metacharacters)
        where dst will point to

    DST is the path to a folder that is the root of the tree
        whose leaves will be linked to src
    '''
    dst = normalize(dst)

    if not os.path.isdir(dst):
        raise Exception(f'destination \'{dst}\' must be a folder')

    m = _split_and_map(src)
    ids = m.keys()

    for current, subdirs, aa in os.walk(dst):
        if not _is_leaf(subdirs, ids):
            continue

        # Obtain already linked sources or still not linked depending if
        # linking or unlinking
        if clear:
            ln_ids = _ids_linked(subdirs, ids)
        else:
            ln_ids = _ids_not_linked(subdirs, ids)

        for i in ln_ids:
            src_base_path = m[i]
            src_path = os.path.join(src_base_path, i)
            ln_src = os.path.relpath(src_path, normalize(current))
            ln_dst = os.path.join(current, i)

            if clear:
                os.unlink(ln_dst)
            else:
                os.symlink(ln_src, ln_dst)


if __name__ == '__main__':
    link_tree()
