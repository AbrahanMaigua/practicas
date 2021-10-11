from tkinter import *

# configuraciones de la raiz
root = Tk()
root.title("Agenda")
root.resizable(1, 1)
# root.iconbitmap("nombre.ico")

# frame marcos
# hijos de root
frame = Frame(root, width=480, height=320)

# enpaqueta la nueva ventana
# la posicion por defeto de los frames sera aliniados
# al centro arriba
# esto lo podemos cambiar con [N,S,E,W,NE...]
# O izquierda, derecha, ariba, abajo 
frame.pack(side=RIGHT) # a la derecha al medio
frame.pack(anchor=SE) #  surerte abajo a la derecha


"""
frame.pack(fill="x") # ancho del padre
frame.pack(fill="x") # alto del padre
frame.pack(fill="both") # ambos
frame.pack(fill="both", expand=1) # expandirse para ocupar el espacio total




"""
# cabiar color de fondo
frame.config(bg="#E3F646")
# frame.config(width=480, height=320)

# tamaço del border
frame.config(bd=10)
# tipo de cursor
frame.config(cursor="")
# relive
frame.config(relief="sunken")


# wigets




# finlailzamos el bucle de la aplicacion
root.mainloop()