#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

from lib.Console import Console




print("h")
c = Console(50, 5)

c.clearScreen()
c.print("Done", "Black", "Red")

print("\n\n")

