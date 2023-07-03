from tkinter import *
from formularioReserva import formulario_reserva
from formularioHabitacion import formulario_habitaciones
from formularioHuesped import formulario_huesped
from formularioUsuario import formulario_usuario





def menu():
    ventana = Tk()
    ventana.geometry('900x650')

    ventana.title('Hotel Duerme Bien App')
    ventana.iconbitmap('images/logo.ico')

    texto = Label(ventana, text='Bienvenido a Duerme Bien App')
    texto.config(
            fg='white',
            bg='black',
            padx=200,
            pady=30,
            font=('Century Gothic', 24)
            )
    texto.grid(row=0, column=0, columnspan=3)



    boton = Button(ventana, text='Registro de Usuario' , command = formulario_usuario)
    boton.grid(row=3, column=1)
    boton.config(padx=15, pady=15, font=('Century Gothic', 16))

    boton = Button(ventana, text='Registro de Huesped' , command = formulario_huesped)
    boton.grid(row=4, column=1)
    boton.config(padx=15, pady=15, font=('Century Gothic', 16))

    boton = Button(ventana, text='Cargar Habitacion' , command= formulario_habitaciones)
    boton.grid(row=5, column=1)
    boton.config(padx=15, pady=15, font=('Century Gothic', 16))

    boton = Button(ventana, text='Registro de Reserva' , command = formulario_reserva)
    boton.grid(row=6, column=1)
    boton.config(padx=15, pady=15, font=('Century Gothic', 16))


    ventana.mainloop()