#!/usr/bin/env python3
from ceefax import config, Ceefax
from os.path import expanduser, join, isdir
import sys
import os

config.ceefax_path = os.path.dirname(os.path.realpath(__file__))
config.pages_dir = os.path.join(config.ceefax_path, "pages")
config.NAME = "28JHFAX"

import config as _c

for i, j in _c.__dict__.items():
    setattr(config, i, j)

test = None

for i,a in enumerate(sys.argv):
    if a in ["-t","--test","-T"] and i+1 < len(sys.argv):
        test = sys.argv[i+1]

c = Ceefax(test)
c.begin()
