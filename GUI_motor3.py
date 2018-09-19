# -* coding: utf-8 -*-
'''
Created on April, 23, 2017

Author: jsha
'''

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image
#from PIL import ImageTk, Image
import os, glob
import dcmotor2

class Movement_Control(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()
        dcmotor2.cleanup()
        dcmotor2.init_set()		

    def initUI(self):
        self.master.title("Rover Control GUI")
        self.pack(fill=BOTH, expand = True)
		
#	self.columnconfigure(1, weight=1)
#	self.rowconfigure(2, weight=1)
        self.area = LabelFrame(self, text='Direction Control')
        self.area.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        
        self.area2 = LabelFrame(self, text='Movement Control')
        self.area2.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.area3 = LabelFrame(self, text='Setting Control')
        self.area3.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        self.area4 = LabelFrame(self, text='Display Status')
        self.area4.grid(row=0, column=4, columnspan=7, rowspan=7, padx=10, pady=10, sticky=E)

#	'Direction & Angle & Command'
        self.direction = StringVar()
        direct_chosen = ttk.Combobox(self.area, text='direction', width=6, textvariable=self.direction, state='readonly')
        direct_chosen['values'] = ('Right', 'Left')
        direct_chosen.grid(row=1, column=0, padx=5)
        direct_chosen.current(0)

        self.angle = StringVar()
        angle_chosen = ttk.Combobox(self.area, text='angle', width=6, textvariable=self.angle, state='readonly')
        angle_chosen['values'] = ('10', '30', '50', '70', '90')
        angle_chosen.grid(row=1, column=1, padx=5)
        angle_chosen.current(0)

        btn_direction = Button(self.area, text='Direction', width=10, command=self.goto_direction)
        btn_direction.grid(row=1, column=2, padx=5)

#	Movement Control 
        self.speed = StringVar()
        speed_chosen = ttk.Combobox(self.area2, text='speed', width=6, textvariable=self.speed, state='readonly')
        speed_chosen['values'] = ('Low', 'High')
        speed_chosen.grid(row=3, column=0, padx=5, pady=5)
        speed_chosen.current(0)
		
        btn_forward = Button(self.area2, text='Forward', command=self.go_forward)
        btn_forward.grid(row=3, column=2, pady=5)
        
        btn_backward = Button(self.area2, text='Backward', command=self.go_backward)
        btn_backward.grid(row=3, column=3, pady=5)
        
        btn_stop = Button(self.area2, text='STOP', width=19, command=self.stop)
        btn_stop.grid(row=4, column=2, columnspan=2, padx=5) 

#	Setting Control
        btn_init = Button(self.area3, text='Init_Set', width=12, command=self.init_set)
        btn_init.grid(row=6, column=1, columnspan=2, padx=5)

        btn_cleanup = Button(self.area3, text='Clean_Up', width=12, command=self.cleanup)
        btn_cleanup.grid(row=6, column=3, columnspan=2, padx=5)

#	Display Status
        scrol_w = 50
        scrol_h = 15 
        self.scr = scrolledtext.ScrolledText(self.area4, width=scrol_w, height=scrol_h, wrap=WORD)
        self.scr.grid(column=4, columnspan=4)

# functions
    def goto_direction(self):
        RL = self.direction.get()
        ANGL = self.angle.get()
        dcmotor2.direction(RL, ANGL)
        self.scr.insert(INSERT, 'To the ' + RL + ' with angle ' + ANGL + ' degree \n')
    
    def go_forward(self):
        SP = self.speed.get()
        dcmotor2.forward(SP)
        self.scr.insert(INSERT, 'Go Forward with ' + SP + ' speed \n')

    def go_backward(self):
        SP = self.speed.get()
        dcmotor2.backward(SP)
        self.scr.insert(INSERT, 'Go Backward with ' + SP + ' speed \n')

    def stop(self):
        dcmotor2.stop()
        self.scr.insert(INSERT, 'The Rover Stopped \n')

    def cleanup(self):
        dcmotor2.cleanup()
        self.scr.insert(INSERT, 'System CleanUp!! \n')
#        self.scr.insert(END, 'Ending System CleanUp!! \n')

    def init_set(self):
        dcmotor2.init_set()
        self.scr.insert(INSERT, 'System Initialization Completed!! \n')
	
def main():
    root = Tk()
    root.geometry("700x280+300+300")
    app = Movement_Control(root)
    app.mainloop()
		
if __name__ == '__main__' :
    main()
