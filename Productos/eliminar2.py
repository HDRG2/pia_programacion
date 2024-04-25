from tkinter import *
from tkinter import ttk

def eliminar_producto(root,productos_menu,main_menu):
    tree = ttk.Treeview(root)
    tree["columns"]=("columna1","columna2","columna3","columna4","columna5")
    
    def previous_page():
        destroy_elements()
        productos_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        button_regresar.destroy()
        nombre_buscar.destroy()
        nombre.destroy()
        button_Buscar.destroy()
        
    
    def Boton_Buscar():
        print("Boton de busqueda precionado")
        # tree.insert("",1,text="L1", values=("1","uno","dos"))
        # tree.insert("",2,text="L2", values=("2","tres","cuatro"))
        # tree.insert("",3,text="L3", values=("3","cinco","seis"))
        # tree.insert("",4,text="L4", values=("4","siete","ocho"))
        # tree.insert("",5,text="L5", values=("5","nueve","diez"))
       
    
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
    
    button_Buscar = Button(root,text="Buscar",command=lambda: Boton_Buscar())
    button_Buscar.place(x=135,y=90)
    
    # # Formatear cada columna
    # tree.column("columna1", width=100)
    # tree.column("columna2", width=100)
    # tree.column("columna3", width=100)
    
    # # Crear los encabezados de las columnas
    # tree.heading("columna1", text="Columna 1")
    # tree.heading("columna2", text="Columna 2")
    # tree.heading("columna3", text="Columna 3")
    
    tree.column("columna1",width=20)
    tree.column("columna2",width=10)
    tree.column("columna3",width=10)
    tree.column("columna4",width=10)
    tree.column("columna5",width=10)
    
    tree.heading("columna1",text="1")
    tree.heading("columna2",text="2")
    tree.heading("columna3",text="3")
    tree.heading("columna4",text="4")
    tree.heading("columna5",text="5")
    
    tree.pack(side='top',expand=True)
    
    datos = [("dato 1","dato 2","dato 3"),("dato 4","dato 5","dato 6"),("dato 7","dato 8","dato 9"),("dato 7","dato 8","dato 9"),("dato 7","dato 8","dato 9")]
    for i in datos:
        tree.insert("","end",values= i)

    # tree.pack()
        
   
   
   
    
   
    
    
