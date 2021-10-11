from tkinter import *

# configuraciones de la raiz
root = Tk()
root.title("Agenda")
root.resizable(1, 1,)
root.config(width=500, height=700)
# label
# label = Label(Frame, text="hollo World")
# label.pack()
# anchor= n, ne, e, se, s, sw, w, nw, or center
label = Label(root, text="Bienvenido a la agenda", height=5 )
label.pack(anchor="center")
label.config(font=("Bauhaus 93 Regular", 24))

texto = StringVar()
texto.set("un nuevo texto")
# anadiendo una variable de texto 
label.config(textvariable=texto)


root.mainloop()