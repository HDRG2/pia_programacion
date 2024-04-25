from tkinter import Button
from Productos.agregar import agregar_producto
from Productos.ver_productos import ver_producto
from Productos.eliminar import eliminar_producto

def productos_menu(root, main_menu):
    def destroy_elements():
        button_agregar.destroy()
        # button_editar.destroy()
        button_eliminar.destroy()
        button_ver_productos.destroy()
        button_regresar.destroy()
    
    def previous_page():
        print("si toque el boton(productos_menu)")

        destroy_elements()
        main_menu(root)
       
    def agregar(root):
        destroy_elements()
        #1.- Pasamos la ventana root 
        #2.- Es la pagina a la que regresaremos si damos click en el boton de regresar
        #3.- Es ka pagina a la que la pagina a la que volveremos debe regresar
        agregar_producto(root,productos_menu, main_menu)
      
    def eliminar(root):
        destroy_elements()
        eliminar_producto(root,productos_menu,main_menu)
    
    def editar(root):
        destroy_elements()
        ver_producto(root,productos_menu,main_menu)
   
    root.title("Productos")
     
    button_agregar = Button(root, text="Agregar", command=lambda: agregar(root))
    button_agregar.grid(row=3, column=0)
    button_agregar.place(x=100, y=100)
    
    # button_editar = Button(root, text="Editar", command=lambda: editar(root))
    # button_editar.grid(row=3, column=0)
    # button_editar.place(x=100, y=150)
    
    button_eliminar = Button(root, text="Eliminar", command=lambda: eliminar(root))
    button_eliminar.grid(row=3, column=0)
    button_eliminar.place(x=100, y=150)
    
    button_ver_productos = Button(root, text="Ver Productos", command=lambda: editar(root))
    button_ver_productos.grid(row=3, column=0)
    button_ver_productos.place(x=100, y=200)
   
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    
    


