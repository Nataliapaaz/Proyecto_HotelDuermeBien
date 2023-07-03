from tkinter import *
from ventanaMenu import menu


def cerrarVentana():
    ventana.destroy()
    menu()


ventana = Tk()
ventana.geometry('700x400')

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

# ---- U S U A R I O -----
#label para el campo de texto (usuario)
label = Label(ventana, text='Usuario')
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto (usuario)
campoUsuario = Entry(ventana)
campoUsuario.grid(row=3, column=1, padx=5, pady=5)

# ---- C O N T R A S E Ñ A -----
#label para el campo de texto (contraseña)
label = Label(ventana, text='Contraseña')
label.grid(row=4, column=0, padx=5, pady=5)
    
#campo de texto (contraseña)
campoContrasena = Entry(ventana)
campoContrasena.grid(row=4, column=1, padx=5, pady=5)

#Este boton ENVIAR, deberia poder mandar los datos del usuario a la base de datos
boton = Button(ventana, text='Enviar', command = cerrarVentana)
boton.grid(row=5, column=1)
boton.config(padx=10, pady=10)

marco = Frame(ventana, width=250, height=50)
marco.config(bg='lightblue')
marco.grid(row=6)


# textoPie = Label(marco, text='Todos los derechos reservados')
# textoPie.config(
#             bg='lightblue',
#             font=('Century Gothic', 11),
#             height=10,
#             width=30,
#             anchor=CENTER)
# textoPie.grid(row=6, column=1, columnspan=3, sticky=S)

#Esto hace que se ejecute la ventana
ventana.mainloop()
