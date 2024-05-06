from tkinter import *
from tkinter import ttk , Entry
from db.Productos2.select_product import  select_product

def eliminar_producto(root,productos_menu,main_menu):
    datos = [('Id', ''),
            ('NomProducto',''),
            ('precio',''),
            ('existencia',''),
            ('idTipoProducto','')]
    
    def previous_page():
        destroy_elements()
        productos_menu(root,main_menu)
        
    def destroy_elements():
        titulo.destroy()
        button_regresar.destroy()
        nombre_buscar.destroy()
        nombre.destroy()
        button_Buscar.destroy()
        table.destroy()
        button_eliminar.destroy()
        
    def boton_buscar():
        bd_data = select_product(nombre.get())
        datos[0] = ("Id", bd_data[0])
        datos[1] =  ('NomProducto',bd_data[1])
        datos[2] = ('precio',bd_data[2])
        datos[3] = ('existencia',bd_data[3])
        datos[4] = ('idTipoProducto',bd_data[4])
        fill_table()
    
    def borrar_datos():
        datos[0] = ("Id",'')
        datos[1] =  ('NomProducto','')
        datos[2] = ('precio','')
        datos[3] = ('existencia','')
        datos[4] = ('idTipoProducto','')
        fill_table()
            
    def fill_table():
            # Limpia la tabla
        for item in table.get_children():
            table.delete(item)
                
        # Inserta los nuevos datos en la tabla
        for dato in datos:
            table.insert('', 'end', values=dato)

    root.title("Eliminando Producto")
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.place(x=0,y=0)
    
    titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
    titulo.place(x=110,y=35)
    
    nombre_buscar = Label(root, text="idProducto:", bg="gray")
    nombre_buscar.place(x=30,y=65)
    nombre = Entry(root)
    nombre.place(x=100,y=65)
    
    button_Buscar = Button(root,text="Buscar",command= lambda: boton_buscar())
    button_Buscar.place(x=135,y=90)
    
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



   
   
    
   
    
    
