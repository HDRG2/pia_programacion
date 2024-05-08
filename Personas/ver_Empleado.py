from tkinter import *
from tkinter import ttk

def ver_empleado(root,empleados_menu,main_menu):
    root.geometry("770x400")
    def previous_page():
        print("si toque el boton")  
        destroy_elements()
        empleados_menu(root,main_menu)
   
    def destroy_elements():
        titulo.destroy()
    
    root.title("Mostrando Empleado")
    
    titulo = Label(root,text="VER EMPLEADOS",bg="gray",font=("Arial",15))
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
    titulo.place(x=300,y=40)
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    table = ttk.Treeview(root, columns=('IdEmpleado','Nombre','ApPat','ApMat','FecNac','Curp','Rfc','Telefono','Correo'), show="headings")
    table.heading('IdEmpleado', text="IdEmpleado")
    table.heading('Nombre', text="Nombre")
    table.heading('ApPat', text="ApPat")
    table.heading('ApMat', text="ApMat")
    table.heading('FecNac', text="FecNac")
    table.heading('Curp', text="Curp")
    table.heading('Rfc', text="Rfc")
    table.heading('Telefono', text="Telefono")
    table.heading('Correo', text="Correo")

    table.column('IdEmpleado', width=80)
    table.column('Nombre', width=80)
    table.column('ApPat', width=80)
    table.column('ApMat', width=80)
    table.column('FecNac', width=80)
    table.column('Curp', width=80)
    table.column('Rfc', width=80)
    table.column('Telefono', width=80)
    table.column('Correo', width=80)
    
    table.place(x=20, y=120)

    
    
    
    
    
    
    

        
    
        


        
        
    
    