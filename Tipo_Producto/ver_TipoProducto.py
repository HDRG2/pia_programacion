from tkinter import * 
from tkinter import ttk
from db.TipoProductoDB.select_ver_TipoProducto import mostrar_tipo_producto

def ver_tipo_producto(root, Tipoproduct_menu, main_menu):
    get_tipo_producto_data()
    tipo_productos = mostrar_tipo_producto()
    root.geometry("350x400")
    
    def previous_page():
        destroy_elements()
        Tipoproduct_menu(root, main_menu)
        
    def destroy_elements():
        titulo.destroy()
        button_regresar.destroy()
        table.destroy()        
            
    root.title("Tipo de producto en Pantalla")
  
    titulo = Label(root, text="VER TIPO PRODUCTO", bg="gray", font=("Arial", 13))
    titulo.place(x=60, y=30)
    
    button_regresar = Button(root, text="<==", command=lambda: previous_page())
    button_regresar.place(x=0, y=0)
    
    table = ttk.Treeview(root, columns=('idTipoProducto', 'descripsion'), show="headings",)
   
    table.heading('idTipoProducto', text="idTipoProducto")
    table.heading('descripsion', text="descr")
    table.column('idTipoProducto', width=100)
    table.column('descripsion', width=140)

    if tipo_productos:
        for tipo_producto in tipo_productos:
            table.insert('', 'end', values=tipo_producto)
    
    table.place(x=50, y=90)
    
def get_tipo_producto_data():
    perro = mostrar_tipo_producto()
    print("miperro:",perro[0])
        