from tkinter import *

# configuraciones de la raiz
root = Tk()
font = "Bell MT"

"""
Importante solo puedes utilizar grid() si vas
no puedes utilizar grid y pack() al mismo tiempo
"""

labelName = Label(root, text="usuario")
labelName.grid(row=2, column=1, sticky="W", padx=5, pady=5)
labelName.config(font=(font, 18))

entryName = Entry(root)
entryName.grid(row=2, column=2, sticky="W", padx=5, pady=5)
entryName.config(justify="left", state="normal")

labelpass = Label(root, text="Password")
labelpass.grid(row=3, column=2, sticky="W", padx=5, pady=5)
labelpass.config(font=(font, 18))

entrypass = Entry(root)
entrypass.grid(row=3, column=2, sticky="W", padx=5, pady=5)
entrypass.config(justify="left", state="normal", show="*")


# justify= left, right, or center
# state=disabled, normal, or readonly
# show=*


# finalizamos el bucle 
root.mainloop()