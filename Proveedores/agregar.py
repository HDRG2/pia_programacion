from tkinter import *

def agregar_proveedores(root,proveedores_menu,main_menu):
    def previous_page():
        destroy_elements()
        proveedores_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre.destroy()
        button_regresar.destroy()
        nombre_label.destroy()
            
           
    root.title("Agregando Proveedor")
  
    titulo = Label(root,text="PROVEEDOR",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))

    nombre_label = Label(root, text="RFCProveedor:", bg="gray")
    nombre_label.grid(row=1, column=0, pady=(10,0))
    nombre = Entry(root)
    nombre.grid(row=1,column=1,pady=(10,0))
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
      