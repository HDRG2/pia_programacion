from tkinter import *
from tkinter import ttk
from db.TipoProductoDB.select_TipoProducto import select_tipoProducto
from db.TipoProductoDB.delete_TipoProducto import delet_TipoProducto

tipoproducto_to_delete = []
tipoproducto_name = ""
def eliminar_TipoProducto(root,Tipoproduct_menu,main_menu):
    
    datos = [('Id', ''),
            ('descr',''),
            ]
    
    def previous_page():
        destroy_elements()
        Tipoproduct_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre.destroy()
        button_regresar.destroy()
        nombre_label.destroy() 
        button_buscar.destroy()
        table.destroy()
        button_eliminar.destroy()
    

    
    def boton_buscar():
        bd_data = select_tipoProducto(nombre.get())
        datos[0] = ("Id", bd_data[0])
        datos[1] = ("descr",bd_data[1])  
             
           # Limpia la tabla
        for item in table.get_children():
            table.delete(item)
                
        # Inserta los nuevos datos en la tabla
        for dato in datos:
            table.insert('', 'end', values=dato)
            
    def borrar_datos ():
        delet_TipoProducto(nombre.get())
        datos[0] = ("Id",'')
        datos[1] =  ('descr','')
       
        
        for item in table.get_children():
            table.delete(item)
            
        for dato in datos:
            table.insert('', 'end', values=dato)
     
        
    root.title("Eliminando TipoProducto")
    
    titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
    titulo.place(x=60,y=35)
   
    nombre_label = Label(root, text="IdTipo:", bg="gray")
    nombre_label.place(x=30,y=70)
    nombre = Entry(root)
    nombre.place(x=90,y=70)
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    button_buscar = Button(root,text= "Buscar",command=lambda:boton_buscar())
    button_buscar.place(x=135,y=90)
    
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
