from tkinter import *
root = Tk()
root.title("Mi Primer Ventana")
root.geometry("500x300") # Dimensiones de la ventana
root.resizable(TRUE, FALSE) # Permitir o no redimensionar la ventana
icono = PhotoImage(file="yahoo.png") # Ruta icono de la ventana
root.iconphoto(True, icono) # Icono de la ventana
root.config(bg="#41644A", cursor="hand2") # Color de fondo y cursor







root.mainloop()