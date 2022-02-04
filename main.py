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


#Print something that is not going to be shown
print("h")

#Create a console 
c = Console(height= 6)

#remove all printed
print(c.clearScreen()) 

#Print a frame once /----\
c.frame(0,0, 15, 3)
c.frame(16,0, 15, 6)

#Print a title once
c.printAt("Sin", x=6, y=1, color="Blue", background="Black")
c.printAt("Cos", x=16+6, y=1, color="Red", background="Black")


#Create a value
value = c.createValue("Sin", "m", decimals=2, x=2, y=2, color="Green", background="Black", detail=1)
value2 = c.createValue("Cos", "m", decimals=2, x=17, y=2, color="Red", background="Black", detail=3)


for n in range(100):
    sensorValue = math.sin(n*(3.14*2.0)/5)
    value.set(sensorValue)
    value2.set(1.0-sensorValue)
    c.show()
    #print("other that is printed " + str(n))
    #print("during the program runs")
    


#https://en.wikipedia.org/wiki/ANSI_escape_code
"""for r in range(0, 5):
    
    print(ANSIEscape.getResetCode())
    for g in range(0, 5):
        for b in range(0, 5):
            print(ANSIEscape.getColorBackgroundColorRGB(r,g,b) + "Hej", end='')
print(ANSIEscape.getResetCode() + " ")"""