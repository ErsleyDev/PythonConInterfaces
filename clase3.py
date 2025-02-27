from tkinter import *

root = Tk()
root.title("Posicion")
root.geometry("400x200")
root.config(bg="#41644A")
root.resizable(0,0)


def saludo():
    print("Hola")

def minimizar():
    root.iconify()


etiqueta1 = Label(root, text="Saludo desde aquí")
etiqueta1.place(x=30, y=50)


etiqueta2 = Label(root, text="Minimizar desde aquí")
etiqueta2.place(x=30, y=100)


boton1 = Button(root, text="Haz click aquí para saludar", command=saludo)
boton1.place(x=200, y=50)

boton2 = Button(root, text="Haz click aquí para minimizar", command=minimizar)
boton2.place(x=200, y=100)






#etiqueta = Label(root, text="Etiqueta")
#etiqueta.place(x=30, y= 40)
#etiqueta.grid(row=0, column=0)

#boton1 = Button(root, text="Boton")
#boton1.grid(row=0, column=1)


root.mainloop()