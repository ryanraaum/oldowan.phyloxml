"""This is the oldowan.phyloxml package."""

import os

VERSION = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION')).read().strip()

__all__ = ['phyloxml']

try:
    from oldowan.phyloxml.phyloxml import phyloxml
except:
    from phyloxml import phyloxml
