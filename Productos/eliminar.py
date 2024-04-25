from tkinter import *
from tkinter import ttk

def eliminar_producto(root,productos_menu,main_menu):
    tree = ttk.Treeview(root)
    tree["columns"]=("uno","dos","tres")
    
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
    
    tree.column("#0",width=270,minwidth=270,stretch=tk.NO)
    tree.column("#1",width=150,minwidth=150,stretch=tk.NO)
    tree.column("#2",width=400,minwidth=200)
    tree.column("#3",width=80,minwidth=50,stretch=tk.NO)
    
    tree.heading("#0",text="idProducto:",anchor=tk.W)
    tree.heading("#1",text=)

       
        
   
   
   
    
   
    
    
