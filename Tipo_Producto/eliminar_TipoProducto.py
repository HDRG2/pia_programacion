from tkinter import *

def eliminar_TipoProducto(root,Tipoproduct_menu,main_menu):
    def previous_page():
        destroy_elements()
        Tipoproduct_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        nombre.destroy()
        button_regresar.destroy()
        nombre_label.destroy() 
        
    root.title("Eliminando el Tipo de Producto")
    
    titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
    titulo.place(x=110,y=35)
   
    nombre_label = Label(root, text="IdTipo:", bg="gray")
    nombre_label.place(x=30,y=70)
    nombre = Entry(root)
    nombre.place(x=90,y=70)
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)