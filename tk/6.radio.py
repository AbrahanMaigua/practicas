from tkinter import *

def selet():
	monitor.config(text="opciones %s %s " %(opciones.get(), notificaciones.get()))


root = Tk()
root.geometry("400x600")
root.title("radiol")
root.resizable(1,1)
root.config(bd=15)

opciones = IntVar()
monitor = Label(root)
monitor.pack()

Radiobutton(root, text="Hombre",value=0, variable=opciones, command=selet ).pack()
Radiobutton(root, text="mujer",value=1, variable=opciones, command=selet ).pack()
Radiobutton(root, text="Deseo",value=2, variable=opciones, command=selet ).pack()



root.mainloop()