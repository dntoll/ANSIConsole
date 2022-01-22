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
from lib.ANSIEscape import ANSIEscape



print("h")
c = Console(50, 5)

print(c.clearScreen())
c.frame()
c.printAt("TopLeft", 21, 1, "Blue", "Black")
c.printAt("BottomRight", 38, 4, "Black", "Green")

for n in range(5):
    c.printAt("Done " + str(n), 5, 4, "Red", "Black")
    c.show()
    c.clear()


#https://en.wikipedia.org/wiki/ANSI_escape_code
for r in range(0, 5):
    
    print(ANSIEscape.getResetCode())
    for g in range(0, 5):
        for b in range(0, 5):
            print(ANSIEscape.getColorBackgroundColorRGB(r,g,b) + "Hej", end='')
print(ANSIEscape.getResetCode() + " ")