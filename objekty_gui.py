import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
import turtle as t
#import objekty
from tkinter import *

class Objekty:
    def __init__(self):
        pass
        

class Ctverec(Objekty):

    def __init__(self,strana_a):
        self.strana_a = strana_a

    def draw(self,vykres,volba,strana_a):
        
        self.t=t.RawTurtle(vykres)
        self.volba = volba
        self.strana_a = strana_a
        
        #self.strana_a = strana_a
        for ii in range (4):
            self.t.forward(self.strana_a)
            self.t.left(90)
        
       


class ObjektyGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #self.ctverec = ctverec
        self.parent.title('Výpočet objemu a obsahu')
        #self.parent.config(bg='grey')
        self.create_widgets()
        self.vykres = self.platno


  
    def create_widgets(self):
        #self.volba = StringVar
        #prvni label
        self.label_hlavni = ttk.Label(root, text = 'Výpočet objemu a obsahu')
        self.label_hlavni.grid(row = 0, column = 0, columnspan = 3,rowspan=1)
        self.label_hlavni.config(font=('Arial',14,'bold'),foreground='green')
        """  self.logo = PhotoImage(file='python_logo.gif')
        self.resized_logo = self.logo.subsample(8, 8) 
        self.label_hlavni.config(image=self.resized_logo)
        self.label_hlavni.config(compound='left')"""

        #druhy label
        self.label_pokyn = ttk.Label(root, text = 'Vyber geometrický objekt')
        self.label_pokyn.grid(row = 1, column = 0, columnspan=3)
        self.label_hlavni.config(font=('Arial',12,'bold'),foreground='green',background='white')

        #combo pro výběr objektu
        self.seznam_objektu = tk.StringVar()
        self.combobox_objekt = ttk.Combobox(root, textvariable=self.seznam_objektu)
        self.combobox_objekt.grid(row=2, column = 0,columnspan=3,sticky='N')
        self.combobox_objekt.config(values=('ctverec', 'obdelnik','uhelnik'))



        #potvrzeni volby z comba
        self.button_volbaobj = ttk.Button(root, text = "Vyber objekt", command = self.menu_objektu)
        self.button_volbaobj.grid(row=3, column=0, columnspan=3, sticky=W+E)
    
        #canvas
        self.platno = tk.Canvas(root, width=640,height=600,background='white')
        self.platno.grid(row=2, rowspan=12,column=3, columnspan=13)

       
    def menu_objektu(self):
        self.volba = self.seznam_objektu.get()
        if self.volba == "ctverec":
            self.strana_zadani = tk.Label(root, text="Zadej délku strany 'a'", width=15)
            self.strana_zadani.grid(row=5, column=0, sticky=W)
            self.delka_zadani = ttk.Entry(root)
            self.delka_zadani.grid(row=6, column=0, sticky=W)
            self.button_potvrdstranu  = ttk.Button(root, text = "Potvrdit", command = self.draw_confirmed )
            self.button_potvrdstranu.grid(row=7, column=0, sticky=W)
            #self.strana_a = self.delka_zadani.get()
            
        else:
            pass
        

    def draw_confirmed(self):
        self.strana_a = self.delka_zadani.get()
        print(f"strana_a je {self.strana_a}")
        try:
            self.strana_a = int(self.strana_a)
        except ValueError:
            print("error")
        ctverec = Ctverec(self.strana_a)
        self.platno.delete("all")
        ctverec.draw(self.platno,self.volba,self.strana_a)
        #self.strana_a = float(self.strana_a)
        #self.menu_objektu()
        #object_to_draw = Ctverec(self.strana_a)
        



    def draw_object(self):
       #volba = self.seznam_objektu.get()
        

        try: 
            
            self.platno = Canvas.delete(ALL) # se to pokouším smazat aby to bylo čisté před kreslením i pro další kreslení
        finally:
            if volba == 'ctverec':
                self.ctverec.draw(ctverec,self.platno,volba,self.strana_a)
                
            elif volba == 'obdelnik':
                self.ctverec.draw(self.platno, volba)
            elif volba == 'uhelnik':
                self.ctverec.draw(self.platno, volba)






if __name__ == "__main__":             
    root = tk.Tk()
    app = ObjektyGUI(root)
    root.mainloop()
    

