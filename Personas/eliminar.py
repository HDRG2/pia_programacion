from tkinter import *
from tkinter import ttk
from db.PersonasDB.select_persona import select_persona
from db.PersonasDB.delete_persona import delet_persona

persona_to_delete = []
persona_name = ""
def eliminar_empleado(root,empleado_menu,main_menu):
    
    datos = [('id',''),
             ('Nombre',''),
             ('apPat',''),
             ('apMat',''),
             ('fecNac',''),
             ('curp',''),
             ('rfc',''),
             ('tel',''),
             ('correo',''),
             ]
    def previous_page():
        destroy_elements()
        empleado_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre.destroy()
        button_regresar.destroy()
        nombre_label.destroy() 
        button_buscar.destroy()
        table.destroy()
        button_buscar.destroy()
        button_eliminar.destroy()
    
    def boton_buscar():
        bd_data = select_persona(nombre.get())
        datos[0] = ("id",bd_data[0])
        datos[1] = ("Nombre",bd_data[1])
        datos[2] = ("apPat",bd_data[2])
        datos[3] = ("apMat",bd_data[3])
        datos[4] = ("fecNac",bd_data[4])
        datos[5] = ("curp",bd_data[5])
        datos[6] = ("rfc",bd_data[6])
        datos[7] = ("tel",bd_data[7])
        datos[8] = ("correo",bd_data[8])
        
        #Para limpiar la tabla
        print("No se encontraron Datos")
        for item in table.get_children():
            table.delete(item)
        
        for dato in datos:
            table.insert('','end', values=dato)
        
    
    def borrar_datos():
        delet_persona(nombre.get())
        datos[0] = ("id",'')
        datos[1] = ("Nombre",'')
        datos[2] = ("apPat",'')
        datos[3] = ("apMat",'')
        datos[4] = ("fecNac",'')
        datos[5] = ("curp",'')
        datos[6] = ("rfc",'')
        datos[7] = ("tel",'')
        datos[8] = ("correo",'') 
        
        for item in table.get_children():
            table.delete(item)
        
        for dato in datos:
            table.insert('','end',values=dato)  
            
    root.title("Eliminando Usuario")
    titulo = Label(root,text="ELIMINAR",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
    
    nombre_label = Label(root,text="idPersona:",bg="gray")
    nombre_label.grid(row=1,column=0,pady=(10,0))
    nombre = Entry(root)
    nombre.grid(row=1,column=1,pady=(10,0))

    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    button_buscar = Button(root,text="Buscar",command=lambda: boton_buscar())
    button_buscar.place(x=125,y=75)
    
    table = ttk.Treeview(root, columns=('Encabezado', 'Informacion'), show="headings")
    table.heading('Encabezado', text="Encabezado")
    table.heading('Informacion', text="Informacion")
    
    table.column('Encabezado',width=150)
    table.column('Informacion',width=150)
    
    for dato in datos:
        table.insert('','end',values=dato)
    
    table.place(x=0, y=150)
    button_eliminar = Button(root,text="Eliminar",command=lambda: borrar_datos())
    button_eliminar.place(x=240,y=390)
