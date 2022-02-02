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
import math
import utime


print("h")
c = Console(50, 6)

print(c.clearScreen())
c.frame()
c.printAt("TopLeft", 21, 1, "Blue", "Black")
c.printAt("BottomRight", 38, 4, "Black", "Green")
value = c.createValue("Sine", "mm", 2, 3, 2, "Red", "Black")

for n in range(100):
    sensorValue = math.sin(n*(3.14*2.0)/20)
    value.set(sensorValue)
    c.show()
    c.clear()


#https://en.wikipedia.org/wiki/ANSI_escape_code
"""for r in range(0, 5):
    
    print(ANSIEscape.getResetCode())
    for g in range(0, 5):
        for b in range(0, 5):
            print(ANSIEscape.getColorBackgroundColorRGB(r,g,b) + "Hej", end='')
print(ANSIEscape.getResetCode() + " ")"""