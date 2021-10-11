import tkinter

from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np 


class Editor(object):
	"""docstring for Editor"""
	def __init__(self, master):
		self.master = master

	def visualizar(self):
		global cap
		if cap is not None:
			ret, frame = cap.read()
			if rest is True:
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				im = Image.fromarray(frame)
				img = ImageTk.PhotoImage(image=im)

				iblvideo.configure(image=img)
				iblvideo.image = img
				iblvideo.afer(10, visualizar)
			else:
				iblvideo.image = ""
				cap.realase()


	def stop(self):
		global cap
		cap.realase()
		


	def gui(self, master):
		pass

		
