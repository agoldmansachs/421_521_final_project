#Python code for Shaken Not Stirred by AGoldmanSachs

#First import relevant modules. 
from Tkinter import * #GUI module
from ttk import * 
import os
from printrun.printcore import printcore #RAMBo module
from printrun import gcoder #GCode module
import subprocess
import math

#Calculate number of times the motor must run through the gcode file depending on the time selected by the user.  
def timecalcz(valuez):
        global timecalc1       
        if valuez=="12 hours (recommended)":
                timecalc1 = math.floor(12*60*60/2.135)
        elif valuez=="14 hours":
                timecalc1 = math.floor(14*60*60/2.135)
        else:
                timecalc1 = math.floor(.002*60*60/2.135)
        return

#Calls pronterface and executes shaking function. 
def shaker(*args):
	timecalc = int(timecalc1) #Makes the loop calculation into a number. 
        path = "./Gcode/shake" #Sets the path name of the gcode file. 

	#Finds the port that the RAMBo connected to and develops the full path name that pronterface can read. 
        def get_serial_port():
                b=os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()
                print b
                return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

        #Loop that sends gcode file to pronterface.        
        for i in range(timecalc):
                path2=path+".gcode"

                #Check to see if gcode file exists in the appropriate directory or if it was accidentally placed elsewhere/deleted. 
                check=os.path.exists(path2)
                print(check)
                if check==True:
                        command = "python printcore.py {0} {1}.gcode".format(get_serial_port(), path)
                        subprocess.call(command, shell=True)
                else:
                        print("Gcode file is not present in the appropriate ")
        return

#Function that tells user how many cups of grounds and water to add to the mason jar dependent on their strength preferences. 
#Outputs to a textbox emnbedded in the GUI.
def ingredients(value):
        if value=="Very Strong":
                textbox.insert(END, str("\nAdd 4 cups of water and 1.5 cups of coffee grounds"))
                print(textbox.get(1.0,END))                
        elif value=="Strong":
                textbox.insert(END, str("\nAdd 4 cups of water and 1.25 cups of coffee grounds"))
                print(textbox.get(1.0,END))
        elif value=="Mild":
                textbox.insert(END, str("\nAdd 4 cups of water and 1 cup of coffee grounds"))
                print(textbox.get(1.0,END))
        elif value=="Weak":
                textbox.insert(END, str("\nAdd 4 cups of water and 0.75 cups of coffee grounds"))
                print(textbox.get(1.0,END))
        else:
                textbox.insert(END, str("\nAdd 4 cup of water and 0.5 cups of coffee grounds"))
                print(textbox.get(1.0,END))
        return
#Function that tells user what temperature of water to use dependent on their acidity preferences.
#Outputs into the same textbox as the function ingredients outputs to. 
def acid(value):
        if value=="Yes":
                textbox.insert(END, str("\nAdd hot water"))
                print(textbox.get(1.0,END))
        else:
                textbox.insert(END, str("\nAdd room temperature water"))
                print(textbox.get(1.0,END))
        return

#Defines the GUI window. 
root = Tk()
root.title("Shaken Not Stirred")

mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Sets the dropdown menus and which function they access. 
variablez = StringVar(root)
strength=OptionMenu(mainframe, variablez, "", "12 hours (recommended)", "14 hours", "0.002 hours (test)", command=timecalcz).grid(column=2, row=3, sticky=(W,E))

variable = StringVar(root)
strength=OptionMenu(mainframe, variable, "", "Very Strong", "Strong", "Mild", "Weak", "Very Weak", command=ingredients).grid(column=2, row=5, sticky=(W,E))

acidity = StringVar(root)
strength=OptionMenu(mainframe, acidity, "", "Yes", "No", command=acid).grid(column=2, row=6, sticky=(W,E))

#Defines the labels for each line in the window. 
Label(mainframe, text="Cold Brew Time (in hours) =").grid(column=1, row=3, sticky=E)
Label(mainframe, text="Strength of Cold Brew").grid(column=1, row=5, sticky=E)
Label(mainframe, text="Acidity").grid(column=1, row=6, sticky=E)
      
#Define your button to start shaking.
Button(mainframe, text="SHAKE!",command=shaker).grid(column=3, row=7, sticky=(E, S))

#Spaces out each thing placed in the window. 
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#Places textbox. 
textbox=Text(root)
textbox.grid(column=0,row=8)

root.mainloop()
