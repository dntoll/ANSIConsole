#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#


class Console:
    #https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#8-colors
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = {
            "Black": "\u001b[30m",
            "Red": "\u001b[31m",
            "Green": "\u001b[32m",
            "Yellow": "\u001b[33m",
            "Blue": "\u001b[34m",
            "Magenta": "\u001b[35m",
            "Cyan": "\u001b[36m",
            "White": "\u001b[37m",
            "Reset": "\u001b[0m" 
        }
        self.background = {
            "Black": "\u001b[40m",
            "Red": "\u001b[41m",
            "Green": "\u001b[42m",
            "Yellow": "\u001b[43m",
            "Blue": "\u001b[44m",
            "Magenta": "\u001b[45m",
            "Cyan": "\u001b[46m",
            "White": "\u001b[47m",
            "Reset": "\u001b[0m" 
        }

        "\u001b[1000D"

        return
    
    def.show(self):
        script =""
        script += self.clearScreen()
        script += self.goToX0Y0()
        
        return
        
    def print(self, text, color="White", background="Black"):
        print(self.background[background] + self.color[color] + text + self.color["Reset"], end='')
    
    def goToX0Y0(self):
        return "\u001b[0;0H"

    def clearScreen(self):
        return "\u001b[2J"


    