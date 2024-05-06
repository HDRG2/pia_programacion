from tkinter import *
from Empleados.agregar import agregar_empleado
from Empleados.eliminar import eliminar_empleado
#from Empleados.ver_empleado import ver_empleado


def empleados_menu(root, main_menu):
    def destroy_elements():
        button_agregar.destroy()
        button_eliminar.destroy()
        #button_ver_Empleado.destroy()
        button_regresar.destroy()
        
    def previous_page():
        print("si toque el boton(empleadosmenu)")

        destroy_elements()
        main_menu(root)
        
    def agregar(root):
        destroy_elements()
        agregar_empleado(root,empleados_menu,main_menu)
        
    def eliminar(root):
        destroy_elements()
        eliminar_empleado(root,empleados_menu,main_menu)
        
    #def ver_empleado(root):
        #destroy_elements()
        #ver_empleado(root,empleados_menu,main_menu)
        
           
    root.title("Empleados")
     
    button_agregar = Button(root,text="Agregar", command=lambda: agregar(root))
    button_agregar.grid(row=3,column=0)
    button_agregar.place(x=100,y=100)
    
    button_eliminar = Button(root,text="Eliminar", command=lambda: eliminar(root))
    button_eliminar.grid(row=3,column=0)
    button_eliminar.place(x=100,y=150)
    
 
    #button_ver_Empleado = Button(root,text="Ver empleado", command=lambda: ver_empleado(root))
    #button_ver_Empleado.grid(row=3,column=0)
    #button_ver_Empleado.place(x=100,y=200)
    
    button_regresar = Button(root,text= "<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    
    
    
    
    
    

        
 
 