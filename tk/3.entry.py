from tkinter import *


# configuraciones de la raiz
root = Tk()
root.title("Agenda")
root.resizable(1, 1,)

font = "Bell MT"

encabezado = Label(root, text="Bienvenido")
# -after, -anchor, -before, -expand, -fill, 
# -in, -ipadx, -ipady, -padx, -pady, or -side
encabezado.pack(fill="x", anchor="center" )
encabezado.config(font=("Bell MT", 18) ,height=3, width=27)

 """
tkinter.TclError: cannot use geometry manager 
grid inside . which already has slaves managed by pack

stackoverflow.com/

import Tkinter as tk
import ttk

class app(object):
	def __init__(self, master, **kwargs):
		self.master = master
		self.create_text()

	def create_text():
		self.textBox = tk.text(master, height=10, width=79, wrap='wold')
		vertscroll = tkk.Scroll(command=self.textbox.yview)
		vertscroll.confing(yscrollcommand=vertscroll.set)
		self.textbox.grid(column=0, row=0)
		self.vertscroll.grid(column=1, row=0, sticky='NS')


root = tk.TK()
app = app(root)
app.mainloop()




 """
labelName = Label(root, text="Nombre")
labelName.grid()
# labelName.config(font=(font, 10))

entryName = Entry(root)
entryName.grid()
# entryName.config()

label = Label(root)
label.pack()
label.config(height=10, width=27)


# # finalizamos el bucle 
root.mainloop()