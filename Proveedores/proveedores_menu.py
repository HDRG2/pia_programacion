# from tkinter import *
# from Proveedores.agregar import agregar_proveedores
# from Proveedores.eliminar import eliminar_Proveedores

# def proveedores_menu(root,main_menu):
#     def destroy_elements():
#         button_agregar.destroy()
#         # button_editar.destroy()
#         button_eliminar.destroy()
#         # button_ver_proveedor.destroy()
#         button_regresar.destroy()
    
#     def previous_page():
#         destroy_elements()
#         main_menu(root)
    
#     def agregar(root):
#         destroy_elements()
#         agregar_proveedores(root,proveedores_menu,main_menu)
        
        
#     def Eliminar(root):
#         destroy_elements()
#         eliminar_Proveedores(root,proveedores_menu,main_menu)
    
#     root.title("Proveedores")
    
#     button_agregar = Button(root, text="Agregar", command=lambda: agregar(root))
#     button_agregar.grid(row=3, column=0)
#     button_agregar.place(x=100, y=100)
    
#     # button_editar = Button(root, text="Editar", command=lambda: editar(root))
#     # button_editar.grid(row=3, column=0)
#     # button_editar.place(x=100, y=150)
    
#     button_eliminar = Button(root, text="Eliminar", command=lambda: Eliminar(root))
#     button_eliminar.grid(row=3, column=0)
#     button_eliminar.place(x=100, y=150)
    
#     # button_ver_proveedor = Button(root, text="Ver Proveedor", command=lambda: editar(root))
#     # button_ver_proveedor.grid(row=3, column=0)
#     # button_ver_proveedor.place(x=100, y=250)
   
#     button_regresar = Button(root,text="<==",command=lambda: previous_page())
#     button_regresar.grid(row=2,column=0,padx=0,pady=0)
#     button_regresar.place(x=0,y=0)
    
    
     
