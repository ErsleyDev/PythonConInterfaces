from tkinter import *

root = Tk()

root.title("Mi Primer Ventana")

root.geometry("500x300") # Dimensiones de la ventana

icono = PhotoImage(file="yahoo.png") # Ruta icono de la ventana

root.iconphoto(True, icono) # Icono de la ventana

# Valores boleanos en tkinter se pueden usar como True =  0, False = 1...  (x,y) si no queremos que se pueda agrandar ponemos false, y vicveversa
root.resizable(0,0)

# Color de fondo de la ventana. se puede usar el nombre del color o el codigo hexadecimal... También se puede cambiar la forma del cursor
root.config(bg="#41644A", cursor="boat") 









root.mainloop()