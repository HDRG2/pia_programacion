from tkinter import *
from Tipo_Producto.agregar_TipoProducto import agregar_TipoProducto
from Tipo_Producto.eliminar_TipoProducto import eliminar_TipoProducto
from Tipo_Producto.ver_TipoProducto import ver_tipo_producto



def TipoProduct_menu(root,main_menu):
    root.geometry("300x500")
    def destroy_elements():
        button_agregar.destroy()
        # button_editar.destroy()
        button_eliminar.destroy()
        button_ver_TipoProducto.destroy()
        button_regresar.destroy()
    
    def previous_page():
        destroy_elements()
        main_menu(root)
    
    def agregar(root):
        destroy_elements()
        agregar_TipoProducto(root,TipoProduct_menu,main_menu)
        
        
    def eliminar(root):
        destroy_elements()
        eliminar_TipoProducto(root,TipoProduct_menu,main_menu)
    
    def mostrar_tipoproducto(root):
        destroy_elements()
        ver_tipo_producto(root,TipoProduct_menu,main_menu)
        
        
    root.title("TIPO PRODUCTO")
     
    button_agregar = Button(root, text="Agregar", command=lambda: agregar(root))
    button_agregar.grid(row=3, column=0)
    button_agregar.place(x=100, y=100)
    
    # button_editar = Button(root, text="Editar", command=lambda: editar(root))
    # button_editar.grid(row=3, column=0)
    # button_editar.place(x=100, y=150)
    
    button_eliminar = Button(root, text="Eliminar", command=lambda: eliminar(root))
    button_eliminar.grid(row=3, column=0)
    button_eliminar.place(x=100, y=150)
    
    button_ver_TipoProducto = Button(root, text="VerTipoProducto", command=lambda: mostrar_tipoproducto(root))
    button_ver_TipoProducto.grid(row=3, column=0)
    button_ver_TipoProducto.place(x=100, y=200)
    
    
   
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
