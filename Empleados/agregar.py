from tkinter import *

def agregar_empleado(root,empleados_menu,main_menu):
    def previous_page():
        print("si toque el boton")
        destroy_elements()
        empleados_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre_id.destroy()
        nombre_empleado.destroy()
        ApellidoPat.destroy()
        ApellidoMat.destroy()
        nombre_empleado.destroy()
        FecNac.destroy()
        curp.destroy()
        rfc.destroy()
        telefono.destroy()
        Correo.destroy()
        button_regresar.destroy()
        nombre_label.destroy()
        nombre_label2.destroy() 
        nombre_label3.destroy()
        nombre_label4.destroy()
        nombre_label5.destroy()
        nombre_label6.destroy()
        nombre_label7.destroy()
        nombre_label8.destroy()
        nombre_label9.destroy()
        
        
        
        
    root.title("Agregando Empleado")
    
    titulo = Label(root,text="EMPLEADO",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
   
    nombre_label = Label(root,text="idEmpleado:",bg="gray")
    nombre_label.grid(row=1,column=0,pady=(10,0))
    nombre_id = Entry(root)
    nombre_id.grid(row=1,column=1,pady=(10,0))
    
    nombre_label2 = Label(root,text="Nombre:",bg="gray")
    nombre_label2.grid(row=2,column=0,pady=(10,0))
    nombre_empleado = Entry(root)
    nombre_empleado.grid(row=2,column=1,pady=(10,0))
    
    nombre_label3 = Label(root,text="Apellido Paterno:",bg="gray")
    nombre_label3.grid(row=3,column=0,pady=(10,0))
    ApellidoPat = Entry(root)
    ApellidoPat.grid(row=3,column=1,pady=(10,0))
    
    nombre_label4 = Label(root,text="Apellido Materno:",bg="gray")
    nombre_label4.grid(row=4,column=0,pady=(10,0))
    ApellidoMat = Entry(root)
    ApellidoMat.grid(row=4,column=1,pady=(10,0))
    
    nombre_label5 = Label(root,text="Fecha de Nacimiento:",bg="gray")
    nombre_label5.grid(row=5,column=0,pady=(10,0))
    FecNac = Entry(root)
    FecNac.grid(row=5,column=1,pady=(10,0))
    
    nombre_label6 = Label(root,text="curp:",bg="gray")
    nombre_label6.grid(row=6,column=0,pady=(10,0))
    curp = Entry(root)
    curp.grid(row=6,column=1,pady=(10,0))
    
    nombre_label7 = Label(root,text="rfc:",bg="gray")
    nombre_label7.grid(row=7,column=0,pady=(10,0))
    rfc = Entry(root)
    rfc.grid(row=7,column=1,pady=(10,0))
    
    nombre_label8 = Label(root,text="telefono:",bg="gray")
    nombre_label8.grid(row=8,column=0,pady=(10,0))
    telefono = Entry(root)
    telefono.grid(row=8,column=1,pady=(10,0))
    
    nombre_label9 = Label(root,text="Correo",bg="gray")
    nombre_label9.grid(row=9,column=0,pady=(10,0))
    Correo = Entry(root)
    Correo.grid(row=9,column=1,pady=(10,0))
    
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
       
    
    