import tkinter

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

ruta = "D:/img/img-articulo-1.jpg"

# position text frame
Label(root, text="image button",
 font=("", 10)).pack(side=TOP, padx=4, pady=10)

# image

photo = PhotoImage(file=ruta)
resize= photo.subsample(1, 2)

Button(root, image=resize).pack(side=BOTTOM,pady=5)

root.mainloop()
