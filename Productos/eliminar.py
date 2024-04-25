from tkinter import *
from tkinter import messagebox, ttk

def eliminar_producto(root,productos_menu,main_menu):
   def previous_page():
       destroy_elements()
       productos_menu(root,main_menu)
    
   def destroy_elements():
       titulo.destroy()
       button_regresar.destroy
       nombre_buscar.destroy()
       nombre.destroy()
       button_Buscar.destroy()
    
   def Buscar():
       print("Boton de busqueda precionado")
    
   def Eliminar():
       print("Eliminar")
        
        
   root.title("Eliminando Producto")
  
   titulo = Label(root,text="ELIMINAR ",bg="gray",font=("Arial",13))
   titulo.place(x=110,y=35)
   
   nombre_buscar = Label(root, text="idProducto:", bg="gray")
   nombre_buscar.place(x=30,y=65)
   nombre = Entry(root)
   nombre.place(x=100,y=65)
    
   button_regresar = Button(root,text="<==",command=lambda: previous_page())
   button_regresar.grid(row=2,column=0,padx=0,pady=0)
   button_regresar.place(x=0,y=0)
   
   button_Buscar = Button(root,text="Buscar",command=lambda: Buscar())
   button_Buscar.place(x=135,y=90)
   
   tabla = ttk.Treeview(root,columns=('idProducto','NomProducto','precio','existecia','idTipoPorducto'),show='headings')
   tabla.heading('idProducto',text='idProducto')
   tabla.heading('NomProducto',text='NomProducto')
   tabla.heading('existencia',text='existencia')
   tabla.heading('idTipoProducto',text='idTipoProducto')
   
   
   

       
        
   
   
   
    
   
    
    
