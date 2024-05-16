from tkinter import *

def usuarios_menu(root,main_menu):
    
    def destroy_elements():
        button_regresar.destroy()
        
    
    def previous_page():
        print("Si se toco el boton")
        destroy_elements()
        main_menu(root)
    
    
    root.title("USUARIOS")
    

    button_regresar = Button(root,text="<==",command=lambda: previous_page())
    button_regresar.grid(row=2,column=0,padx=0,pady=0)
    button_regresar.place(x=0,y=0)
    

    
     
