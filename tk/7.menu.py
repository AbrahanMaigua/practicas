from tkinter import *

root = Tk()
root.geometry("200x400")
root.title("Menu")
root.resizable(1,1)
root.config(bd=15)


menubar = Menu(root)  
root.config(menu=menubar)

file = Menu(menubar, tearoff=0)
file.add_command(label="open file")
file.add_command(label="new file")
file.add_command(label="save")
file.add_command(label="save with")
file.add_separator()
file.add_command(label="exit", command=root.qui)

menubar.add_cascade(label="file", menu=file)


edit = Menu(menubar,  tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Copy")
edit.add_command(label="Cut")
edit.add_command(label="Paste")


Help = Menu(menubar,  tearoff=0)
menubar.add_cascade(label="Help", menu=Help)
Help.add_command(label="doc")
Help.add_command(label="license")

Help.add_separator()
Help.add_cascade(label="About..")








root.mainloop()