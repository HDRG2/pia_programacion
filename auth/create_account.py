from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk 

def create_account(root, login):
    
    def previous_page():
        print("si toque el boton")
        destroy_elements()
        login(root)
    
    def destroy_elements():
        nombre_label.destroy()
        apellido_pat.destroy()
        apellido_mat.destroy()
        nombre.destroy()
        frame.destroy()
        apellido_pat_label.destroy()
        apellido_mat_label.destroy()
        # years_combobox.destroy()
        button_regresar.destroy()
        telefono.destroy()
        FechaNacimiento.destroy()
        Correo.destroy()
        

    # def toggle_calendar():
    #     if not fecha_nacimiento.winfo_ismapped():  # Verifica si el calendario está oculto
    #         fecha_nacimiento.grid(row=7, column=0, padx=10, pady=10) # Muestra el calendario
    #     else:
    #         fecha_nacimiento.grid_forget()  # Oculta el calendario
    
  
    # Creamos un marco para contener los elementos del formulario
    frame = Frame(root, width=400, height=400,pady=80, padx=90)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centramos el marco en la ventana

    nombre_label = Label(frame, text="Nombre")
    nombre_label.grid(row=0, column=0,pady=0)  # Añadido relleno a la etiqueta
    nombre = Entry(frame)
    nombre.grid(row=1, column=0,pady=5)# Añadido relleno al campo de entrada
    

    apellido_pat_label = Label(frame, text="Apellido Paterno")
    apellido_pat_label.grid(row=2, column=0,pady=0)  # Añadido relleno a la etiqueta
    apellido_pat = Entry(frame)
    apellido_pat.grid(row=3, column=0,pady=5)  # Añadido relleno al campo de entrada

    apellido_mat_label = Label(frame, text="Apellido Materno")
    apellido_mat_label.grid(row=4, column=0,pady=0)  # Añadido relleno a la etiqueta
    apellido_mat = Entry(frame)
    apellido_mat.grid(row=5, column=0,pady=5)  # Añadido relleno al campo de entrada
    
    telefono = Label(frame, text="telefono")
    telefono.grid(row=6,column=0,pady=0)
    telefono = Entry(frame)
    telefono.grid(row=7,column=0,pady=5)
    
    Correo = Label(frame, text="Correo")
    Correo.grid(row=8,column=0,pady=0)
    Correo = Entry(frame)
    Correo.grid(row=9,column=0,pady=5)
    
    FechaNacimiento = Label(frame, text="Fecha de Nacimiento")
    FechaNacimiento.grid(row=10,column=0,pady=0)
    
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    years = [str(year) for year in range(1990,2026)]
    
    years_combobox = ttk.Combobox(frame, values=years, state="readonly",width=10)
    years_combobox.set("Año")
    years_combobox.place(x=-72,y=280)
    
    names_months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    months_number = range(1, 13)
    months = dict(zip(names_months,months_number))
    
    months_combobox = ttk.Combobox(frame,values=list(months.keys()), state= "readonly",width=10)
    months_combobox.set("Mes")
    months_combobox.place(x=20,y=280)
    
    days = [str(day) for day in range(1,32)]
    
    days_combobox = ttk.Combobox(frame, values=days, state="readonly",width=10)
    days_combobox.set("Dia")
    days_combobox.place(x=110,y=280)
    
    




    # button = Button(frame, text="Mostrar/ocultar calendario", command=toggle_calendar)
    # button.grid(row=6, column=0, padx=10, pady=10)

    # global fecha_nacimiento  # Hacemos que fecha_nacimiento sea global para que sea accesible desde toggle_calendar
    # fecha_nacimiento = Calendar(frame, selectmode="day", year=1999, month=9, day=30)


    # password_label = Label(frame, text="Contraseña")
    # password_label.grid(row=2, column=0, padx=10, pady=0)  # Añadido relleno a la etiqueta
    
    # password = Entry(frame, show="*")  # Establecemos el atributo show para mostrar "*" en lugar de los caracteres
    # password.grid(row=3, column=0, padx=10, pady=0)  # Añadido relleno al campo de entrada
    
    # button = Button(frame,text="Iniciar Sesion")
    # button.grid(row=4,column=0,padx=0,pady=0)
    
    # create_account_label = Label(frame, text ="Crear Cuenta", fg="blue", cursor="hand2")
    # create_account_label.grid(row=5, column=0, padx=10, pady=0)


