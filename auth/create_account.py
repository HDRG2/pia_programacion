from tkinter import *
from tkcalendar import Calendar
def create_account(root, login):

    def toggle_calendar():
        if not fecha_nacimiento.winfo_ismapped():  # Verifica si el calendario está oculto
            fecha_nacimiento.grid(row=7, column=0, padx=10, pady=10) # Muestra el calendario
        else:
            fecha_nacimiento.grid_forget()  # Oculta el calendario

    # Creamos un marco para contener los elementos del formulario
    frame = Frame(root, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centramos el marco en la ventana

    nombre_label = Label(frame, text="Nombre")
    nombre_label.grid(row=0, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    nombre = Entry(frame)
    nombre.grid(row=1, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada

    apellido_pat_label = Label(frame, text="Apellido Paterno")
    apellido_pat_label.grid(row=2, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    apellido_pat = Entry(frame)
    apellido_pat.grid(row=3, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada

    apellido_mat_label = Label(frame, text="Apellido Materno")
    apellido_mat_label.grid(row=4, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    apellido_mat = Entry(frame)
    apellido_mat.grid(row=5, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada

    button = Button(frame, text="Mostrar/ocultar calendario", command=toggle_calendar)
    button.grid(row=6, column=0, padx=10, pady=10)

    global fecha_nacimiento  # Hacemos que fecha_nacimiento sea global para que sea accesible desde toggle_calendar
    fecha_nacimiento = Calendar(frame, selectmode="day", year=1999, month=9, day=30)    





    # password_label = Label(frame, text="Contraseña")
    # password_label.grid(row=2, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    # password = Entry(frame, show="*")  # Establecemos el atributo show para mostrar "*" en lugar de los caracteres
    # password.grid(row=3, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada
    
    # button = Button(frame,text="Iniciar Sesion")
    # button.grid(row=4,column=0,padx=0,pady=0)
    
    # create_account_label = Label(frame, text ="Crear Cuenta", fg="blue", cursor="hand2")
    # create_account_label.grid(row=5, column=0, padx=10, pady=0)


