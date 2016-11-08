from Tkinter import *
from ttk import * 
from time import strftime, localtime
import os
from printrun.printcore import printcore
from printrun import gcoder
import subprocess

file='shake.gcode'

pathname=os.path.join("/home/pi/Printrun/Gcode",file)
pathname
print(pathname)
