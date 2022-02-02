
from ANSIEscape import ANSIEscape
import math

class ValueView:
    def __init__(self, value):
        self.value = value
    
    def getText(self, number):
        numberFormat = "{:." + str(self.value.decimals) + "f}"
        return  numberFormat.format(number) + self.value.unit

    def get(self, height):
        val = self.value

        ret = ""
        #ret += self.bufferGraph(height)
        ret += ANSIEscape.goToXY(val.x, val.y) + ANSIEscape.getBackgroundColor(val.background) + ANSIEscape.getTextColor(val.color)
        
        
        
        #return ret + ANSIEscape.getResetCode()

        ret += val.title + ": " + self.getText(val.value) + ANSIEscape.goToXY(val.x, val.y+1)
        ret += "max :" + self.getText(val.max) + ANSIEscape.goToXY(val.x, val.y+2)
        ret += "avg :" + self.getText(val.getAverage()) + ANSIEscape.goToXY(val.x, val.y+3)
        ret += "min :" + self.getText(val.min) + ANSIEscape.goToXY(val.x, val.y+4)


        ran = val.max - val.min
        if ran > 0:
            fraktion = (val.value - val.min) / ran
            at = int(10.0 * fraktion)
        else:
            at = 0
        
        ret += "[" + '-' *at + 'O' + '-' * (10-at)  + "]"

        return ret + ANSIEscape.getResetCode()

""" The framerate was too low for this
    def bufferGraph(self, height):
        ret = ""
        left = self.value.x + 20
        top = self.value.y 


        for i in range(0, self.value.buffer.getSize()-1):
            val = self.value.buffer.get(i)
            x = left + i
            vrange = self.value.max - self.value.min
            yscale = height/vrange
            ypos = yscale*(val-self.value.min)
            iypos = math.floor(ypos)

            #self.buffer +=  + text +  _,-^-._
            for y in range(height):
                ret += ANSIEscape.goToXY(x, y) + " "
            ret += ANSIEscape.goToXY(x, iypos) + "x" + ANSIEscape.getResetCode()


        return ret"""