from tkinter import *

# configuraciones de la raiz
root = Tk()
root.title("Agenda")
root.resizable(1, 1,)

font = ("Bradley Hand ITC", 18)


textName = Text(root)
textName.pack(fill="both", expand=1)
textName.config(width=30, height=10, )
textName.config(font=font, bg='#EEEEEE', padx=15, pady=15)



# # finalizamos el bucle 
root.mainloop()