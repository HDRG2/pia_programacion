from tkinter import * 
from tkinter import ttk

def ver_TipoProducto(root,Tipoproduct_menu,main_menu):
    def previous_page():
        destroy_elements()
        Tipoproduct_menu(root,main_menu)
        
    def destroy_elements():
        titulo.destroy()
        # nombre.destroy()
        button_regresar.destroy()
        # nombre_label.destroy()
    
    
    root.title("Tipo de producto en Pantalla")
  
    titulo = Label(root,text="VER TIPO PRODUCTO",bg="gray",font=("Arial",13))
    titulo.place(x=60,y=30)

    # nombre_label = Label(root, text="idTipoProducto:", bg="gray")
    # nombre_label.grid(row=1, column=0, pady=(10,0))
    # nombre = Entry(root)
    # nombre.grid(row=1,column=1,pady=(10,0))
    
    
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)