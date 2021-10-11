import tkinter

from tkinter import *
from PIL import ImageTk, Image

wigth = 100
heigt = 150

def img():
	global wigth
	global heigt

	ruta   = "D:/img/img-articulo-1.jpg"
	Img    = Image.open(ruta)

	size   = Img.resize((wigth, heigt), Image.ANTIALIAS)
	tk_img = ImageTk.PhotoImage(size)



	
	imglabel= tkinter.Label(image=tk_img)
	imglabel.image = tk_img
	# imglabel.afer(10, img)
	# position Image
	imglabel.place(x=50, y=50)
def add():
	global wigth
	global heigt
	global imglabel



	wigth += 10
	heigt += 10
	img()
	print(wigth)

def rest():
	global wigth
	global heigt
	wigth -= 10
	heigt -= 10
	img()
	print(heigt)


root = Tk()
image = img()
while True :
	Button(root, text="+", command=add).pack()
	Button(root, text="-", command=rest).pack()
	del image
	root.mainloop()
