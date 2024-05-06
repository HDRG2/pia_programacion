from tkinter import *
from tkinter import  ttk
from db.Productos2.create_product import create_product

def agregar_producto(root,productos_menu,main_menu):
    def previous_page():
        print("si toque el boton(productos_agregar)")

        destroy_elements()
        productos_menu(root,main_menu)
    
    def destroy_elements():
      titulo.destroy()
      nombre.destroy()
      precio.destroy()
      existencia.destroy()
      button_regresar.destroy()
      nombre_label.destroy()
      nombre_label2.destroy()
      nombre_label3.destroy()
      nombre_label4.destroy()
      combo.destroy()

    def mostrar_seleccion(event):
      seleccion = combo.get()
      print("Seleccione:",seleccion)
    
    def boton_agregar():
      new_product = {
        "name": nombre.get(),
        "precio": precio.get(),
        "existencia": existencia.get(),
        "tipo_producto": combo.get(),
      }
      print("new_products:",new_product)
      bd_data = create_product(new_product)
      print(bd_data)
  
    
        
    root.title("Agregando Producto")
  
    titulo = Label(root,text="PRODUCTO",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))

    nombre_label = Label(root, text="NomProducto:", bg="gray")
    nombre_label.grid(row=1, column=0, pady=(10,0))
    nombre = Entry(root)
    nombre.grid(row=1,column=1,pady=(10,0))
    
    nombre_label2 = Label(root, text="Precio:", bg="gray")
    nombre_label2.grid(row=2, column=0, pady=(10,0))
    precio = Entry(root)
    precio.grid(row=2,column=1,pady=(10,0))
    
    nombre_label3 = Label(root, text="Existencia:", bg="gray")
    nombre_label3.grid(row=3, column=0, pady=(10,0))
    existencia = Entry(root)
    existencia.grid(row=3,column=1,pady=(10,0))
    
    nombre_label4 = Label(root,text="TipoProducto:",bg="gray")
    nombre_label4.place(x=4,y=150)
    
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    button_agregar = Button(root, text="Crear",command=lambda:boton_agregar())
    button_agregar.place(x=100,y=400)
    

    combo = ttk.Combobox(
      state="readonly",
      values=["Materia de Escritura","Papel","Material de oficina","Material escolar","Materiales de Arte","Electronica"]
    )
    combo.place(x=90,y=150)
    combo.bind('<<ComboboxSelected>>',mostrar_seleccion)
    
    
  
    
    
    
    
    
    
    
   
   
        