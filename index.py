#inicio
from tkinter import *
import time

# Configuración de la ventana
root = Tk()
root.title("Mi Primer Ventana")
root.geometry("500x300") # Dimensiones de la ventana
icono = PhotoImage(file="yahoo.png") # Ruta icono de la ventana
root.iconphoto(True, icono) # Icono de la ventana
#root.config(bg="#41644A")




boton1 = Button(root, text="Minimizar", command=root.iconify, bg="red") #Boton para minimizar la ventana
boton1.pack(side=LEFT)

def imprimir():
    label1 = Label(root, text="Imprimiendo...")
    label1.pack()

boton2=Button(root, text="Imprimir", command=imprimir, bg="blue")
boton2.pack(side=RIGHT)





root.mainloop()