#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#
from ANSIEscape import ANSIEscape

class Value:
    def __init__(self, title, unit, decimals, x, y, color, background):
        self.title = title
        self.unit = unit
        self.x = x 
        self.y = y
        self.decimals = decimals
        self.color = color
        self.background = background
        self.value = 0
        self.total = 0
        self.min = None
        self.max = None
        self.numValues = 0

    def getAverage(self):
        return self.total / self.numValues
    
    def set(self, value):
        self.value = value
        self.total += value
        self.numValues += 1
        if self.min == None or self.min > value:
            self.min = value
        if self.max == None or self.max < value:
            self.max = value

class ValueView:
    def __init__(self, value):
        self.value = value
    
    def getText(self, number):
        numberFormat = "{:." + str(self.value.decimals) + "f}"
        return  numberFormat.format(number) + self.value.unit

    def get(self, console):
        val = self.value
        ret = ANSIEscape.goToXY(val.x, val.y) + ANSIEscape.getBackgroundColor(val.background) + ANSIEscape.getTextColor(val.color)
        
        #self.buffer +=  + text + 

        ret += val.title + ": " + self.getText(val.value) + ANSIEscape.goToXY(val.x, val.y+1)
        ret += "max :" + self.getText(val.max) + ANSIEscape.goToXY(val.x, val.y+2)
        ret += "avg :" + self.getText(val.getAverage()) + ANSIEscape.goToXY(val.x, val.y+3)
        ret += "min :" + self.getText(val.min) 

        return ret + ANSIEscape.getResetCode()

class Console:
    #https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#8-colors
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()
        self.values = []
    
    def show(self):

        for val in self.values:
            vv = ValueView(val)
            self.buffer += vv.get(self)
            

        script = ""
       # script += self.clearScreen()
        script += ANSIEscape.goToXY(0,0)
        script += self.buffer

        
        
        print(script+"\n")

    def frame(self, char='*'):
        self.buffer += ANSIEscape.goToXY(0,0)
        self.printAt( '/' + (self.width-2) *  '-' + '\\', 0,0, "Blue", "Black")
        for n in range(2,self.height):
            self.printAt('|', 0, n, "Blue", "Black")
            self.printAt('|', self.width, n, "Blue", "Black")
        self.printAt('\\' + (self.width-2)*'-' + '/', 0, self.height, "Blue", "Black")
        ##for y in range(0, self.height):
        #    self.buffer
    def createValue(self, title, unit, decimals, x, y, color, background):
        val = Value(title, unit, decimals, x, y, color, background)
        self.values.append(val)
        return val
    
    def clearScreen(self):
        print(ANSIEscape.clearScreen())

    def clear(self):
        self.buffer = "";

    def printAt(self, text, x, y, color="White", background="Black"):
        self.buffer += ANSIEscape.goToXY(x, y)
        self.buffer += ANSIEscape.getBackgroundColor(background) + ANSIEscape.getTextColor(color) + text + ANSIEscape.getResetCode()
    
    


    