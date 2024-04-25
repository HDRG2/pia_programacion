from tkinter import *
from tkinter import ttk

def eliminar_producto(root,productos_menu,main_menu):
        
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

    def Boton_Buscar():
        print("Boton de busqueda precionado")
           
    root.title("Eliminando Producto")
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.place(x=0,y=0)
    
    titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
    titulo.place(x=110,y=35)
    
    nombre_buscar = Label(root, text="idProducto:", bg="gray")
    nombre_buscar.place(x=30,y=65)
    nombre = Entry(root)
    nombre.place(x=100,y=65)
        
    button_Buscar = Button(root,text="Buscar",command=lambda: Boton_Buscar())
    button_Buscar.place(x=135,y=90)
    
    table = ttk.Treeview(root, columns=('Encabezado', 'Informacion'), show="headings")
    table.heading('Encabezado', text="Encabezado")
    table.heading('Informacion', text="Informacion")
    
    table.column('Encabezado',width=150)
    table.column('Informacion',width=150)

    
    datos = [('Id', '123'),
            ('Nombre','cocacola'),
            ('Descripcion','Descripcion')]
    
    for dato in datos:
        table.insert('','end',values=dato)
    
    table.place(x=0, y=150)
    


   
   
    
   
    
    
