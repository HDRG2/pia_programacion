from tkinter import *
from tkinter import  ttk

def agregar_producto(root,productos_menu,main_menu):
    def previous_page():
        print("si toque el boton(productos_agregar)")

        destroy_elements()
        productos_menu(root,main_menu)
    
    def destroy_elements():
      titulo.destroy()
      nombre.destroy()
      nombre2.destroy()
      nombre3.destroy()
      button_regresar.destroy()
      nombre_label.destroy()
      nombre_label2.destroy()
      nombre_label3.destroy()
      combo.destroy()
     
    # def show_selection():
    #   selection = combo.get()
    #   messagebox.showinfo(
    #     message=f"El Tipo de Producto que selecciono fue: {selection}"
    #   )
    
    def mostrar_seleccion(event):
      seleccion = combo.get()
      print("Seleccione:",seleccion)
        
    root.title("Agregando Producto")
  
    titulo = Label(root,text="PRODUCTO",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))

    nombre_label = Label(root, text="NomProducto:", bg="gray")
    nombre_label.grid(row=1, column=0, pady=(10,0))
    nombre = Entry(root)
    nombre.grid(row=1,column=1,pady=(10,0))
    
    nombre_label2 = Label(root, text="Precio:", bg="gray")
    nombre_label2.grid(row=2, column=0, pady=(10,0))
    nombre2 = Entry(root)
    nombre2.grid(row=2,column=1,pady=(10,0))
    
    nombre_label3 = Label(root, text="Existencia:", bg="gray")
    nombre_label3.grid(row=3, column=0, pady=(10,0))
    nombre3 = Entry(root)
    nombre3.grid(row=3,column=1,pady=(10,0))
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    combo = ttk.Combobox(
      state="readonly",
      values=["Materia de Escritura","Papel","Material de oficina","Material escolar","Materiales de Arte","Electronica"]
    )
    combo.place(x=90,y=150)
    combo.bind('<<ComboboxSelected>>',mostrar_seleccion)
  
    
    
    
    
    
    
    
   
   
        