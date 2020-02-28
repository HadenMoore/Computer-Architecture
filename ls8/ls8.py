#!/usr/bin/env python3

"""Main."""

import sys
import cpu
from cpu import *

cpu = CPU()

if len(sys.argv) != 2:
    print("ERROR: must have file name")
    sys.exit(1)

cpu.load(sys.argv[1])
cpu.run()