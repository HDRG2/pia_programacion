from tkinter import *
from Productos.products_menu import productos_menu
from Empleados.empleados_menu import empleados_menu
from Proveedores.proveedores_menu import proveedores_menu

def main_menu(root):
    # Obtenemos el objeto Tk llamando a la función tk_main
   
    def destroy_elements():
        boton1.destroy()
        boton2.destroy()
        boton3.destroy()

    def productos():
        destroy_elements()
        productos_menu(root, main_menu)
    
    def empleados():
        destroy_elements()
        empleados_menu(root,main_menu) 
    
    def proveedores():
        destroy_elements()
        proveedores_menu(root,main_menu)

    root.title("Menu")

    boton1 = Button(root, text="Productos", command=productos)
    boton2 = Button(root, text="Empleados", command=empleados)
    boton3 = Button(root, text="Proveedores", command=proveedores)
       
    boton1.grid(row=2, column=0, padx=0, pady=0)
    boton1.grid(row=3, column=0)
    boton1.place(x=100, y=100)
        
    boton2.grid(row=2, column=0, padx=0, pady=0)
    boton2.grid(row=3, column=0)
    boton2.place(x=100, y=150)
        
    boton3.grid(row=2, column=0, padx=0, pady=0)
    boton3.grid(row=3, column=0)
    boton3.place(x=100, y=200)
    #tk_main.mainloop()


   





