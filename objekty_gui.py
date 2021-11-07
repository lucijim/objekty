import tkinter as tk
from tkinter import PhotoImage, ttk
import turtle 
import objekty

class ObjektyGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.parent.title('Výpočet objemu a obsahu')
        #self.parent.config(bg='grey')
        self.create_widgets()
  

    def draw_object(volba):
            if volba == 'ctverec':
                ctverec = objekty.Ctverec(5)
                ctverec.draw()
            elif volba == 'obdelnik':
                obdelnik = objekty.Obdelnik(5,10)
                obdelnik.draw()
            elif volba == 'uhelnik':
                uhelnik = objekty.Uhelnik(5,8)
                uhelnik.draw()
        
    def vyber_obj(self):
        volba = self.seznam_objektu.get() 
        self.draw_object(volba)

    def create_widgets(self):
        #self.volba = StringVar
        #prvni label
        self.label_hlavni = ttk.Label(self.parent, text = 'Výpočet objemu a obsahu')
        self.label_hlavni.grid(row = 0, column = 0, columnspan = 3,rowspan=1)
        self.label_hlavni.config(font=('Arial',14,'bold'),foreground='green')
        self.logo = PhotoImage(file='C:\\Users\\Uzivatel\\Documents\\Chica\\learning\\Tkinter basics\\Ex_Files_Python_GUI_Dev_Tkinter\\Ex_Files_Python_GUI_Dev_Tkinter\\Exercise Files\\Ch03\\python_logo.gif')
        self.resized_logo = self.logo.subsample(8, 8) 
        self.label_hlavni.config(image=self.resized_logo)
        self.label_hlavni.config(compound='left')

        #druhy label
        self.label_pokyn = ttk.Label(self.parent, text = 'Vyber geometrický objekt')
        self.label_pokyn.grid(row = 2, column = 0, columnspan=3)
        self.label_hlavni.config(font=('Arial',12,'bold'),foreground='green',background='white')

        #combo pro výběr objektu
        self.seznam_objektu = tk.StringVar()
        self.combobox_objekt = ttk.Combobox(self.parent, textvariable=self.seznam_objektu)
        self.combobox_objekt.grid(row=3, column = 0,columnspan=3,sticky='N')
        self.combobox_objekt.config(values=('ctverec', 'obdelnik','uhelnik'))

        #potvrzeni volby z comba
        self.button_volbaobj = ttk.Button(self.parent, text = "Vyber objekt")
        self.button_volbaobj.grid(row=3, column=1)
        self.button_volbaobj.config(command = self.vyber_obj)
     

        #canvas
        self.platno = tk.Canvas(self.parent, width=640,height=600,background='white')
        self.platno.grid(row=3,column=3)
        
        s = turtle.TurtleScreen(self.platno)
        t = turtle.RawTurtle(self.platno) 

        t.forward(100)

        
        
    


def main():              
    root = tk.Tk()
    app = ObjektyGUI(root)
    root.mainloop()
    
if __name__ == "__main__": main()
