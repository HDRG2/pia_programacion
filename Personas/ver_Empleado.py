from tkinter import *
from tkinter import ttk
from db.PersonasDB.mostrar_persona import mostrar_persona

def ver_empleado(root,empleados_menu,main_menu):
    get_persona_data()
    personas = mostrar_persona()
    root.geometry("1160x450")
    
    def previous_page():
        print("si toque el boton")  
        destroy_elements()
        empleados_menu(root,main_menu)
   
    def destroy_elements():
        titulo.destroy()
        table.destroy()
        button_regresar.destroy()
        
    
    root.title("Mostrando Empleado")
    
    titulo = Label(root,text="VER EMPLEADOS",bg="gray",font=("Arial",15))
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
    titulo.place(x=500,y=40)
    
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

    table.column('IdEmpleado', width=120)
    table.column('Nombre', width=120)
    table.column('ApPat', width=120)
    table.column('ApMat', width=120)
    table.column('FecNac', width=120)
    table.column('Curp', width=150)
    table.column('Rfc', width=120)
    table.column('Telefono', width=120)
    table.column('Correo', width=120)
    
    if personas:
        for persona in personas:
            table.insert('','end', values=persona)
    
    table.place(x=20, y=120)
    
def get_persona_data():
    persona = mostrar_persona()
    print("persona",persona)

    
    
    
    
    
    
    

        
    
        


        
        
    
    