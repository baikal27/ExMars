#!/usr/bin/python3
# -* coding: utf-8 -*-
'''
Created on April, 21, 2017
Author: jsha
'''

from tkinter import *
#from PIL import Image
from PIL import ImageTk, Image
import os, glob
import hc_sr04

class Sensor_Control(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		master.title("Sensor_Control")
		master.geometry('800x700+0+0')
	
		lbl_1 = Label(master, text = "Camera Snapshot")
		lbl_1.pack(anchor=N, pady=5)

		self.canvas = Canvas(master, width=640, height=480)
		self.canvas.pack()


# display camera_snapshot
		lblfrm = Frame(master)
		lblfrm.pack()
		
		btn_pre = Button(lblfrm, text = 'Pre <<', command = self.disp_prepic, width=10)
		btn_pre.grid(row=0, column=0, padx=5, pady=5)

		self.image =  StringVar()
		txt_picname = Entry(lblfrm, textvariable = self.image, width=10)
		txt_picname.grid(row=0, column=1, padx=5, pady=5)
		self.image.set("")

		btn_post = Button(lblfrm, text = '>> Post', command = self.disp_postpic, width=10)
		btn_post.grid(row=0, column=2)

# shot & reset
		lblfrm2 = Frame(master)
		lblfrm2.pack()

		btn_shot = Button(lblfrm2, text = 'Take a shot', width=50, command=self.takepho)
		btn_shot.grid(row=0, column=0, padx=50, pady=30)

#		btn_shot = Button(lblfrm2, text = 'Erase All', width=10)
#		btn_shot.grid(row=0, column=1)
	
# Ultrasonic Distance meter & Temperature sensor
	#Ultrasonic
		lblfrm3 = Frame(master)
		lblfrm3.pack()

		lbl_Distance = Label(lblfrm3, text = 'Distance')
		lbl_Distance.grid(row=0, column=1)
		
		self.distance = StringVar()
		lbl_Dist_disp = Entry(lblfrm3, textvariable=self.distance, width=10)
		lbl_Dist_disp.grid(row=0, column=2)
		self.distance.set("    cm")

		btn_Distance = Button(lblfrm3, text = 'Ultrasonic Sensor', command=self.ultrasonic_sensor)
		btn_Distance.grid(row=0, column=3)

	# Temperature sensor
#		lbl_Temp = Label(lblfrm3, text = 'Temperature')
#		lbl_Temp.grid(row=1, column=1, padx=10, pady=5)

#		lbl_Temp_disp = Label(lblfrm3, text = 'display')
#		lbl_Temp_disp.grid(row=1, column=2, padx=10, pady=5)

#		btn_Temp = Button(lblfrm3, text = 'Temperature Sensor')
#		btn_Temp.grid(row=1, column=3, padx=10, pady=5)

# funtions

	def takepho(self):
		cam_w = 640
		cam_h = 480

		try :
			list_photonum = glob.glob('*.jpg')
			list_photonum.sort()
			num = int(list_photonum[-1].split('.')[0])
			picname = "%06i.jpg" %(num+1)
#			picname = time.strftime('%Y%m%d-%H%M%S')
			os.system("raspistill -t 1000 -w %i -h %i -o %s" %(cam_w, cam_h, picname))
			self.image.set(picname)

			self.disp_image(picname)
		except:
			num = 0
			picname = "%06i.jpg" %(num+1)
			os.system("raspistill -t 1000 -w %i -h %i -o %s" %(cam_w, cam_h, picname))
			self.image.set(picname)

			self.disp_image(picname)			

	def disp_image(self, path):
		img = ImageTk.PhotoImage(Image.open(path))
		self.canvas.image = img
		self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

	def disp_prepic(self) :
		picname = self.image.get()
		num = int(picname.split('.')[0])
		picname = "%06i.jpg" %(num-1)
		list_photonum = glob.glob("*.jpg")
		if picname in list_photonum :
			self.image.set(picname)
			self.disp_image(picname)
		else : pass

	def disp_postpic(self) :
		picname = self.image.get()
		num = int(picname.split('.')[0])
		picname = "%06i.jpg" %(num+1)
		list_photonum = glob.glob('*.jpg')
		if picname in list_photonum :
			self.image.set(picname)
			self.disp_image(picname)
		else : pass


	def ultrasonic_sensor(self):
		distance_by_ultrasonic = int(hc_sr04.readDistanceCm())
		self.distance.set(str(distance_by_ultrasonic) + ' cm')
#		os.system("python3 /home/pi/Work/Sensor/SuperSonic/hc_sr04.py") 
				

if __name__ == "__main__" :
	root = Tk()
	ap = Sensor_Control(master=root)
	ap.mainloop()	

