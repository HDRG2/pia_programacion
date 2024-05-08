from tkinter import *
from db.PersonasDB.create_persona import create_persona
from utilities.generate_id import generate_id

def agregar_empleado(root,empleados_menu,main_menu):
    def previous_page():
        print("si toque el boton")
        destroy_elements()
        empleados_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre_persona.destroy()
        ApellidoPat.destroy()
        ApellidoMat.destroy()
        FecNac.destroy()
        curp.destroy()
        rfc.destroy() 
        telefono.destroy()
        Correo.destroy()
        button_regresar.destroy()
        button_crear.destroy()
        nombre_label2.destroy() 
        nombre_label3.destroy()
        nombre_label4.destroy()
        nombre_label5.destroy()
        nombre_label6.destroy()
        nombre_label7.destroy()
        nombre_label8.destroy()
        nombre_label9.destroy()
    
    def boton_agregar():
        new_persona = {
            "ID": generate_id(),
            "Nombre":nombre_persona.get(),
            "ApPat":ApellidoPat.get(),
            "ApMat":ApellidoMat.get(),
            "FecNac":FecNac.get(),
            "curp":curp.get(),
            "rfc":rfc.get(),
            "telefono":telefono.get(),
            "correo":Correo.get(),
        }
        print("new_empleado",new_persona)
        bd_data = create_persona(new_persona)
        print(bd_data)
       
           
    root.title("Agregando Empleando")
    
    titulo = Label(root,text="EMPLEADO",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
   
    nombre_label2 = Label(root,text="Nombre:",bg="gray")
    nombre_label2.grid(row=1,column=0,pady=(10,0))
    nombre_persona = Entry(root)
    nombre_persona.grid(row=1,column=1,pady=(10,0))
    
    nombre_label3 = Label(root,text="Apellido Paterno:",bg="gray")
    nombre_label3.grid(row=2,column=0,pady=(10,0))
    ApellidoPat = Entry(root)
    ApellidoPat.grid(row=2,column=1,pady=(10,0))
    
    nombre_label4 = Label(root,text="Apellido Materno:",bg="gray")
    nombre_label4.grid(row=3,column=0,pady=(10,0))
    ApellidoMat = Entry(root)
    ApellidoMat.grid(row=3,column=1,pady=(10,0))
    
    nombre_label5 = Label(root,text="Fecha de Nacimiento:",bg="gray")
    nombre_label5.grid(row=4,column=0,pady=(10,0))
    FecNac = Entry(root)
    FecNac.grid(row=4,column=1,pady=(10,0))
    
    nombre_label6 = Label(root,text="curp:",bg="gray")
    nombre_label6.grid(row=5,column=0,pady=(10,0))
    curp = Entry(root)
    curp.grid(row=5,column=1,pady=(10,0))
    
    nombre_label7 = Label(root,text="rfc:",bg="gray")
    nombre_label7.grid(row=6,column=0,pady=(10,0))
    rfc = Entry(root)
    rfc.grid(row=6,column=1,pady=(10,0))
    
    nombre_label8 = Label(root,text="telefono:",bg="gray")
    nombre_label8.grid(row=7,column=0,pady=(10,0))
    telefono = Entry(root)
    telefono.grid(row=7,column=1,pady=(10,0))
    
    nombre_label9 = Label(root,text="Correo:",bg="gray")
    nombre_label9.grid(row=8,column=0,pady=(10,0))
    Correo = Entry(root)
    Correo.grid(row=8,column=1,pady=(10,0))
    
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    button_crear = Button(root,text="Crear",command=lambda: boton_agregar())
    button_crear.place(x=165,y=300)
    
    
    