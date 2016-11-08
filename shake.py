#Python code for the Robo-Hand GUI

#First import the tkinter modules from Python v.3

from Tkinter import *
from ttk import * 
from time import strftime, localtime
import os
from printrun.printcore import printcore
from printrun import gcoder
import subprocess


#PULLEYCIRC = 39.9925 #mm/rev (Calculated using the pulley pitch diameter)
MOTORSTEPANGLE = 5. #steps/mm

		
	#Send your generated Gcode directly to the printer

def writeGcode(*args):
    #file="/Gcode/shake.gcode"
    #path=os.getcwd()+file
    for i in range(timez.get()):
        command = "python printcore.py shake.gcode".format(os.path.join("/", "dev", "ttyACM0"),"/home/pi/Printrun/Gcode/shake.gcode")
        subprocess.call(command, shell=True)

#Define your mainframe widget that codes for your main window and define its title and grid layout

root = Tk()
root.title("Robo-Hand Control Center")

mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Define the flexion, extension, and repetition entry boxes and place them within the main window's grid layout
repetitions = IntVar()
timez = IntVar()
filename = StringVar()

timez_entry = Entry(mainframe, width=7, textvariable=timez)
timez_entry.grid(column=2, row=3, sticky=(W, E))

filename_entry = Entry(mainframe, width=7, textvariable=filename)
filename_entry.grid(column=2, row=4, sticky=(W, E))

#Define the labels for the previously defined user-input entry boxes

Label(mainframe, text="Shakin' Time =").grid(column=1, row=3, sticky=E)

Label(mainframe, text="Filename").grid(column=1, row=4, sticky=E)

#Define your button to go

Button(mainframe, text="SHAKE!",command=writeGcode).grid(column=3, row=4, sticky=(E, S))

#Shortcuts and running

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


timez_entry.focus()
filename_entry.focus()

root.mainloop()
