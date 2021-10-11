from tkinter import filedialog, messagebox
from tkinter import *

# image 
from PIL import Image,  ImageTk

class App(object):
	"""docstring for ClassName"""
	def __init__(self, master):
		self.master = master
		self.ruta   = ""
		self.menu(self.master)
	
		
	def menu(self, frame):
		# file 
		self.barra  = self.menubar(frame)
		self.File   = self.file(self.barra)
		self.command(self.File, "open", self.open_file)
		self.command(self.File, "view ruta", self.view_ruta)
		self.separator(self.File)
		self.command(self.File, "Exit", frame.quit)
		self.cascade(self.barra, "File", self.File)

	
	def menubar(self, frame):

		# menubar = Menu(frame)
		# root.config(menu=menubar)
		menu = Menu(frame)
		frame.config(menu=menu)
		return menu

	def file(self,barra):
		# file = Menu(menubar, tearoff=0)
		comm = Menu(barra, tearoff=0)

		return comm
	def command(self,menuFile , label, command=None):
		# file.add_command(label="open file")
		menuFile.add_command(label=label, command=command)

	def separator(self,menuFile):
		# file.add_separator()
		menuFile.add_separator()

	def cascade(self,menubar ,label, menu):	
		# menubar.add_cascade(label="file", menu=file)
		menubar.add_cascade(label=label,menu=menu)

	def open_file(self):
		# -defaultextension, -, -initialdir,
		 # -initialfile, -multiple, -parent, -title, or -typevariable
		

		Type = ("jpg","*.jpg",),("all", "*.*")	
		self.ruta = filedialog.askopenfilename(title="Open file", filetypes=Type)
		if self.ruta.count(".jpg") >= 1:
			self.imageView()
		
		return self.ruta

	def imageView(self):
		if self.ruta != "":
			img = Image.open(self.ruta)
			photo = ImageTk.PhotoImage(img)
			self.image = Label(image=photo)
			self.image.image = photo
			self.image.pack()
			print(img)
			self.view_ruta()
		else:
			print("ruta vacioa")

	def view_ruta(self):
		if self.ruta != "":
			print(self.ruta)
			print(self.ruta.count('.jpg'))
		else:
			print("ruta vacioa")


