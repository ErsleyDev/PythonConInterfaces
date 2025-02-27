from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("400x300")



nombre = StringVar()
apellido = StringVar()

nombre.set("Escribe aquí tu nombre") #el .set rellena automáticamente el campo de texto
apellido.set("Escribe aquí tu apellido") #el .set rellena automáticamente el campo de texto

def saludar():
    print(f"Hola {nombre.get()} {apellido.get()}") #get() para obtener el texto de la variable




etiqueta1 = Label(root, text="Escribe aqui tu nombre: ")
etiqueta1.place(x=10, y=10)
entrada1 = Entry(root, textvariable=nombre) #Función entry para ingresar texto/ Y el textVariable para guardar el texto
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text="Escribe aqui tu apellido: ")
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=apellido) #Función entry para ingresar texto
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar ahora", command=saludar)
boton.place(x=10, y=100)



root.mainloop()