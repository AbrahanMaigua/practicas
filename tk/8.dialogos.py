from tkinter import *
from tkinter import messagebox as Messagebox


root = Tk()
root.geometry("200x400")
root.title("Menu")
root.resizable(1,1)
root.config(bd=15)

# showInfo

def show():
	Messagebox.showinfo("Saludos", "Greting")

def warning():
	Messagebox.showwarning("Alerta", "No tines permiso para hacer eso")

def Error():
	Messagebox.showerror("Error", "A ocurido un error")

def ask():
	ret = Messagebox.askquestion("salir", "¿seguro que desea salir?")

	if (ret):
		root.destroy()

from tkinter import colorchooser as ColorChooser

def color_palt():
	color = ColorChooser.askcolor(title="Elegir Color")
	print(color)
from tkinter import filedialog as FileDialog

def open_file():
	# -defaultextension, -, -initialdir,
	 # -initialfile, -multiple, -parent, -title, or -typevariable
	file = FileDialog.askopenfilename(title="open file",
		initialdir="D:",
		 filetypes=({
				 	("jpg","*.jpg",),
					("all", "*.*")	}),
					)
	print(file)

def save():
	# "-modo": must be -confirmoverwrite, -defaultextension,
	 # -filetypes, -initialdir, -initialfile, -parent, -title, or -typevariable
	file = FileDialog.asksaveasfile(title="Gurdar como...",
		mode="wb", defaultextension=".jpg",
		filetypes=({
				 	("jpg","*.jpg",),
					("all", "*.*")	}),
					) 
	if file is not None:
		file.write()
		file.close()

	print(file)

Button(root, text="Info", command=show).pack()
Button(root, text="Alerta", command=warning).pack()
Button(root, text="salir", command=ask).pack()
Button(root, text="color", command=color_palt).pack()
Button(root, text="open", command=open_file).pack()
Button(root, text="save", command=save).pack()





root.mainloop()
