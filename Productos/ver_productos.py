from tkinter import * 
from tkinter import ttk
from db.ProductosDB.mostrar_producto import mostrar_producto

def ver_producto(root,productos_menu,main_menu):
    get_producto_data()
    productos = mostrar_producto()
    root.geometry("600x350")
    
    
    def previous_page():
        destroy_elements()
        productos_menu(root,main_menu)
        
    def destroy_elements():
        titulo.destroy()
        button_regresar.destroy()
        table.destroy()
    
            
    root.title("Mostrando")
  
    titulo = Label(root,text="PRODUCTOS EXISTENTES",bg="gray", font=("Arial",13))
    titulo.place(x=200,y=30)
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.place(x=0,y=0)
    
    table = ttk.Treeview(root,columns=('idProducto','Nombre','Precio','Existencia','idTipoProducto'), show="headings",) 
    table.heading('idProducto',text="idProducto")
    table.heading('Nombre',text="Nombre")
    table.heading('Precio',text="Precio")
    table.heading('Existencia',text="Existencia")
    table.heading('idTipoProducto',text="idTipoProducto")
    table.column('idProducto',width=100)
    table.column('Nombre',width=100)
    table.column('Precio', width=100)
    table.column('Existencia', width=100)
    table.column('idTipoProducto', width=100)
    
    if productos:
        for producto in productos:
            table.insert('','end', values=producto)
    
    table.place(x=40,y=100)
    
def get_producto_data():
    producto = mostrar_producto()
    print("miproducto:",producto)

    
    
   