from tkinter import *


root = Tk()

root.title("agenda")
root.resizable(1, 1)
root.config(bd=15)

def saludo():
	print("Hello World ")

#  backend
def borrar():
	nun1.set("")
	nun2.set("")

def sumar():
	rust = r.set(int(nun1.get())  + int( nun2.get() ))
	print(r)
	borrar()
	

nun1 = StringVar()
nun2 = StringVar()
r 	 = StringVar() 


Label(root, text="\nnumero 1").pack()
Entry(root, justify="center", textvariable=nun1).pack()

Label(root, text="\nnumero 2").pack()
Entry(root, justify="center", textvariable=nun2).pack()

Label(root, text="\nresultado").pack()
Entry(root, justify="center", state=DISABLED, textvariable=r).pack()

Label(root).pack()

Button(root, text="sumar", command=sumar, bd=2, ).pack(side=LEFT)
Button(root, text='greting',command=saludo, bd=2,  ).pack(side=LEFT)





root.mainloop()
