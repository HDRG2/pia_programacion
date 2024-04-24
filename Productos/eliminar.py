from tkinter import *
from tkinter import messagebox, ttk

def eliminar_producto(root,productos_menu,main_menu):
   def previous_page():
       destroy_elements()
       productos_menu(root,main_menu)
    
   def destroy_elements():
       titulo.destroy()
       button_regresar.destroy()
    
     
    
   
    
   root.title("Eliminando Producto")
  
   titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
   titulo.place(x=110,y=35)

#    nombre_label = Label(root, text="NomProducto:", bg="gray")
#    nombre_label.grid(row=1, column=0, pady=(10,0))
#    nombre = Entry(root)
#    nombre.grid(row=1,column=1,pady=(10,0))
    
   button_regresar = Button(root,text="<==",command=lambda: previous_page())
   button_regresar.grid(row=2,column=0,padx=0,pady=0)
   button_regresar.place(x=0,y=0)
   
   

       
        
   
   
   
    
   
    
    
