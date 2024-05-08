from tkinter import *
from main import main_menu
from auth.create_account import create_account
def login(root):
    root.title("Bienvenido!")

    def destroy_elements():
        frame.destroy()

    def iniciar_sesion():
        destroy_elements()
        main_menu(root)
    
    def create_account_form():
        create_account(root,login)


    # Creamos un marco para contener los elementos del formulario
    frame = Frame(root, pady=120,padx=120)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centramos el marco en la ventana

    nombre_label = Label(frame, text="Usuario")
    nombre_label.grid(row=0, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    nombre = Entry(frame)
    nombre.grid(row=1, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada

    password_label = Label(frame, text="Contraseña")
    password_label.grid(row=2, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    password = Entry(frame, show="*")  # Establecemos el atributo show para mostrar "*" en lugar de los caracteres
    password.grid(row=3, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada

    button = Button(frame,text="Iniciar Sesion", command=iniciar_sesion)
    button.grid(row=4,column=0,padx=0,pady=0)
    
    create_account_label = Label(frame, text="Crear Cuenta", fg="blue", cursor="hand2")
    create_account_label.grid(row=5, column=0, padx=10, pady=0)
    create_account_label.bind("<Button-1>", lambda event: create_account_form())  # Utilizamos lambda para pasar la función sin argumentos adicionales
