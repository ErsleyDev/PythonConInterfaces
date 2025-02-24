#inicio
from tkinter import *
import time

# Configuración de la ventana
root = Tk()
root.title("Mi Primer Ventana")
root.geometry("500x300") # Dimensiones de la ventana
icono = PhotoImage(file="yahoo.png") # Ruta icono de la ventana
root.iconphoto(True, icono) # Icono de la ventana





boton1 = Button(root, text="Minimizar", command=root.iconify) #Boton para minimizar la ventana
boton1.pack()




boton2=Button(root, text="Imprimir", command=)
boton2.pack()













root.mainloop()