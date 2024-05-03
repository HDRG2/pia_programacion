from tkinter import Tk
# from main import main_menu
from auth.login import login

root = Tk()

def main_tk():
    root.title("Menu")
    root.config(bg='Gray')
    root.geometry("300x500")
    root.resizable(width=0, height=0)
    # main_menu(root)
    login(root)
    root.mainloop()
    
if __name__ == "__main__":
    main_tk()
 