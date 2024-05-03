from tkinter import *
from Productos.products_menu import productos_menu
from Empleados.empleados_menu import empleados_menu
from Proveedores.proveedores_menu import proveedores_menu
from Tipo_Producto.Tipoprodutc_menu import TipoProduct_menu

def main_menu(root):
    # Obtenemos el objeto Tk llamando a la función tk_main
   
    def destroy_elements():
        boton1.destroy()
        boton2.destroy()
        boton3.destroy()

    def productos():
        print("Destruyendo BOTONES")
        destroy_elements()
        productos_menu(root, main_menu)
    
    def empleados():
        destroy_elements()
        empleados_menu(root,main_menu) 
    
    def proveedores():
        destroy_elements()
        proveedores_menu(root,main_menu)
    
    def TipoProducto():
        destroy_elements()
        TipoProduct_menu(root,main_menu)
        
    
    def close_sesion():
        print("cerrando...")
    
    root.title("Menu")

    boton1 = Button(root, text="Productos", command=productos)
    boton2 = Button(root, text="Empleados", command=empleados)
    boton3 = Button(root, text="Proveedores", command=proveedores)
    boton4 = Button(root, text="Proveedores", command=close_sesion)
    boton5 = Button(root, text="TipoProducto",command=TipoProducto)
       
    boton1.place(x=100, y=100)
    
    boton5.place(x=100,y=150)
        
    boton2.place(x=100, y=200)
        
    boton3.place(x=100, y=250)
    
    

    #tk_main.mainloop()


   





