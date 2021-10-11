from tkinter import *
from tkinter import filedialog, messagebox
from io import open



# ruta

ruta = ""

# file

# open file
def open_file():
	global ruta
	typeFile = ("txt","*.txt"),("All", "*.*"),
		
	if ruta != "":
		ruta = filedialog.askopenfilename(filetype=(typeFile),
			initialdir=".",
			title="Open File"
				)
	
	else:
		ruta = filedialog.askopenfilename(filetype=typeFile,
			initialdir=".",
			title="Open File"
				)
		with open(ruta, "r") as fichero:
			cont = fichero.read()
			texto.delete(1.0, 'end')
			texto.insert("insert", cont)


		root.title(ruta + " - Agenda")

# new file
def new_file():
	global ruta
	ruta = ""
	texto.delete(1.0, "end")
	root.title("Agenda")

# save
def save():
	global ruta
	if ruta != "":
		cont = texto.get(1.0, "end-1c")
		with open(ruta, "w+") as fichero:
			fichero.write(cont)
	else:
		save_with()

# save with
def save_with():
	global ruta
	# -confirmoverwrite, -defaultextension, -filetypes, 
	# -initialdir, -initialfile, -parent, -title, or -typevariable
	ruta = filedialog.asksaveasfilename(title="Save With", defaultextension=".txt")

	if ruta != "":
		cont = texto.get(1.0, "end-1c")
		with open(ruta, "w+") as fichero:
			fichero.write(cont)
	else:
		ruta=""


# edit

#  help
def about():
	messagebox.showinfo("About...", "Agenda V0 - Copyright (C) " )

def doc():
	messagebox.showinfo("doc", "https://github.com/leivakuro765/agendaPersonalizable" )

def lic():
	messagebox.showinfo("Licencia", "licencia libre" )

root = Tk()
root.geometry("300x600")
root.title("Agenda")

menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar, tearoff=0)
file.add_command(label="open file", command=open_file)
file.add_command(label="new file",	command=new_file)
file.add_command(label="save",		command=save)
file.add_command(label="save with",	command=save_with)
file.add_separator()
file.add_command(label="exit", command=root.quit)

menubar.add_cascade(label="file", menu=file)


edit = Menu(menubar,  tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Copy")
edit.add_command(label="Cut")
edit.add_command(label="Paste")


Help = Menu(menubar,  tearoff=0)
menubar.add_cascade(label="Help", menu=Help)

Help.add_command(label="doc", command=doc)
Help.add_command(label="license", command=lic)
Help.add_separator()
Help.add_cascade(label="About..", command=about)

texto =  Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Cosolas", 12))




root.mainloop()