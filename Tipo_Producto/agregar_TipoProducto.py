from tkinter import *
from tkinter import ttk
from db.TipoProductoDB.create_TipoProducto import create_TipoProducto
from utilities.generate_id import generate_id

def agregar_TipoProducto(root,TipoProduct_menu,main_menu):
    def previous_page():
        print("si toque el boton")
        destroy_elements()
        TipoProduct_menu(root,main_menu)
    
    def destroy_elements():
        titulo.destroy()
        # nombre.destroy()
        # nombre_id.destroy()
        nombre_label2.destroy()
        descripcion_entry.destroy()
        button_regresar.destroy()
        # combo.destroy()
        button_agregar.destroy()
        
    # def mostrar_seleccion(event):
    #   seleccion = combo.get()
    #   print("Seleccione:",seleccion)
   
    def boton_agregar():
      descripcion_texto = descripcion_entry.get()
      if not descripcion_texto.strip():
        print("Error: La descripcion no puede estar vacia.")
        return
  
      new_tipoproducto = {
        "ID": generate_id(),
        "descripcion": descripcion_texto,
      }
      print("new_tipoproducto:",new_tipoproducto)
      bd_data = create_TipoProducto(new_tipoproducto)
      print(bd_data)
      
    root.title("Agregando el Tipo de Producto")
    
    titulo = Label(root,text="TIPOPRODUCTO",bg="gray")
    titulo.grid(row=0,column=0,sticky="N",padx=(30,0),pady=(20,0))
    
    nombre_label2 = Label(root,text="descripcion:",bg="gray")
    nombre_label2.grid(row=2,column=0,pady=(10,0))
    descripcion_entry = Entry(root)
    descripcion_entry.grid(row=2,column=1,pady=(10,0))
     
    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    
    button_agregar = Button(root,text="Crear",command=lambda:boton_agregar())
    button_agregar.place(x=160,y=100)
    
  