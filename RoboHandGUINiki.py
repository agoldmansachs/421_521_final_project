# -*- coding: utf-8 -*-
#Python code for the Robo-Hand GUI

#First import the tkinter modules from Python v.3

from Tkinter import *
from ttk import * 
from time import strftime, localtime
import os
from printrun.printcore import printcore
from printrun import gcoder
import subprocess
import math

#Define your date

def dateName():

	dateStr = strftime("%Y-%B-%d", localtime())
	return dateStr

#Define you time

def timeName():
	timeStr = strftime("%I-%M-%S%p", localtime())
	return timeStr

#Initialize your directory for storing your final Gcode

def initGcodeDir(filename):

	dateStr = dateName()
	timeStr = timeName()
	dirPath = "./Gcode/{0}".format(dateStr)
	if not os.path.exists(dirPath): os.makedirs(dirPath)
	filepath = "{0}/{1}{2}".format(dirPath,timeStr,filename)
	return filepath

#Write your Gcode file using the inputs from the GUI

def timecalcz(valuez):
        global timecalc1       
        if valuez=="12 hours (recommended)":
                timecalc1 = math.floor(12*60*60/2.135)
                print(timecalc)
        elif valuez=="14 hours":
                timecalc1 = math.floor(14*60*60/2.135)
                print(timecalc1)
        else:
                timecalc1 = math.floor(.002*60*60/2.135)
                print(timecalc1)
        
def writeGcode(*args):

	#Define your path for saving and pull the numbers that the user input into the GUI to be used for writing Gcode file

	path = initGcodeDir(filename.get())
	configParam = {
			"filenameStr": path,
			"TimeinStr": str(timein.get())
			}

	#Create your Gcode file that will be written to

	try:
		f = open(configParam["filenameStr"] + ".gcode",'w')
	except:
		print("Error - Open")
		error.set("Cannot open" + configParam["filenameStr"] + ".gcode")

	#For loop to write the Gcode commands for the specified number of repetitions
        
	body = ""
	timecalc = int(timecalc1)
	print(timecalc)
	for i in range(timecalc):
                body += "G0 X8 F1000\n"
                body += "G4 P100\n"
                body += "G0 X-8 F1000\n"
                body += "G4 P100\n"			

	f.writelines(body)
	f.close()
        print(path)
        #path = "./Gcode"
	#Send your generated Gcode directly to the printer
        def get_serial_port():
                return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()
        print(get_serial_port())                                
	try:
		command = "python printcore.py {0} {1}.gcode".format(os.path.join(get_serial_port()), path)
		subprocess.call(command, shell=True)
	except Exception:
		pass

def ingredients(value):
        if value=="Very Strong":
                print("Add 1 cup of water and 1.75 cups of coffee grounds")
        elif value=="Strong":
                print("Add 1 cup of water and 1.5 cups of coffee grounds")
        elif value=="Mild":
                print("Add 1 cup of water and 1.25 cups of coffee grounds")
        elif value=="Weak":
                print("Add 1 cup of water and 1 cup of coffee grounds")
        else:
                print("Add 1 cup of water and 0.75 cups of coffee grounds")
        return  
        
#Define your mainframe widget that codes for your main window and define its title and grid layout

root = Tk()
root.title("Robo-Hand Control Center")

mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

filename = StringVar()
timein = StringVar()

variablez = StringVar(root)
variablez.set("Time")
strength=OptionMenu(mainframe, variablez, "12 hours (recommended)", "14 hours", "0.002 hours (test)", command=timecalcz).grid(column=2, row=3, sticky=(W,E))

variable = StringVar(root)
variable.set("Strength")
strength=OptionMenu(mainframe, variable, "Very Strong", "Strong", "Mild", "Weak", "Very Weak", command=ingredients).grid(column=2, row=5, sticky=(W,E))

filename_entry = Entry(mainframe, width=7, textvariable=filename)
filename_entry.grid(column=2, row=6, sticky=(W, E))

timein_entry = Entry(mainframe, width=7, textvariable=timein)
timein_entry.grid(column=2, row=8, sticky=(W, E))

#Define the labels for the previously defined user-input entry boxes

Label(mainframe, text="Cold Brew Time (in hours) =").grid(column=1, row=3, sticky=E)
Label(mainframe, text="Strength of Cold Brew").grid(column=1, row=5, sticky=E)
Label(mainframe, text="Filename").grid(column=1, row=6, sticky=E)
Label(mainframe, text="This is just for debugging").grid(column=1, row=8, sticky=E)
      
#Define your button to go

Button(mainframe, text="SHAKE!",command=writeGcode).grid(column=3, row=7, sticky=(E, S))

#Shortcuts and running

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

filename_entry.focus()

root.mainloop()
