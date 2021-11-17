
from tkinter import *
root = Tk()
root.geometry("300x200")
root.title("Formulario Simple")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))
#-----Seccion de Nombre-----
nombre_label= Label(miFrame, text="Cual es tu nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)
#-----Seccion de Apellido-----
apellido_label=Label(miFrame, text="Cual es tu apellido: ")
apellido_label.grid(row=2, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_Apellido=Entry(miFrame)
cuadro_Apellido.grid(row=2, column=1)
#-----Seccion de Dirección-----
direccion=Label(miFrame, text="Dirección: ")
direccion.grid(row=3, column=0)
direccion.config(padx=10, pady=10)
cuadro_Direccion=Entry(miFrame)
cuadro_Direccion.grid(row=3, column=1)
root.mainloop()