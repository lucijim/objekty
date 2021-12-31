import tkinter as tk
#from tkinter import PhotoImage
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
import turtle as t


#from objekty import Obdelnik

class Objekty:
    def __init__(self):
        #self.pixel_to_cm = 38
        self.objektylist = ['čtverec','obdélník', 'úhelník']
        self.pixel_to_cm = 38

    objekty = ['čtverec', 'obdélník','úhelník']
    
    
        

class Ctverec(Objekty):

    def __init__(self,strana_a):
        
        self.strana_a = strana_a   
        self.pixel_to_cm = 38

    def draw(self,vykres,volba,strana_a):
        
        self.t=t.RawTurtle(vykres)
        self.volba = volba
        self.strana_a = strana_a
        
        #self.strana_a = strana_a
        for ii in range (4):
            self.t.forward(self.strana_a*self.pixel_to_cm)
            self.t.left(90)

class Obdelnik(Objekty):
    def __init__(self,strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b
        self.pixel_to_cm = 38

    def obvod(self):
        return 2*self.strana_a*self.strana_b
    
    def obsah(self):
        return self.strana_a*self.strana_b

    def draw(self,vykres,volba,strana_a, strana_b):
        self.t=t.RawTurtle(vykres)
        self.volba = volba
        self.strana_a = strana_a
        self.strana_b = strana_b

        for ii in range (2):
            self.t.forward(self.pixel_to_cm*self.strana_a)
            self.t.left(90)
            self.t.forward(self.pixel_to_cm*self.strana_b)
            self.t.left(90)

class Uhelnik(Objekty):  
        def __init__(self,strana_a, pocet_uhlu):
            self.strana_a = strana_a
            self.pocet_uhlu = pocet_uhlu
            self.pixel_to_cm = 38

        def draw(self, vykres, volba, strana_a, pocet_uhlu):
            self.t=t.RawTurtle(vykres)
            self.volba = volba
            self.strana_a = strana_a
            self.pocet_uhlu = pocet_uhlu
            for ii in range (self.pocet_uhlu):
                self.t.forward(self.pixel_to_cm*self.strana_a)
                self.t.left(180 - (180 * (1-2/self.pocet_uhlu)))
        


       


class ObjektyGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Výpočet objemu a obsahu')
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
        self.combobox_objekt.config(values=('čtverec', 'obdélník','úhelník'))
       



        #potvrzeni volby z comba
        self.button_volbaobj = ttk.Button(root, text = "Vyber objekt", command = self.menu_objektu)
        self.button_volbaobj.grid(row=3, column=0, columnspan=3, sticky=W+E)
    
        #canvas
        self.platno = tk.Canvas(root, width=640,height=600,background='white')
        self.platno.grid(row=2, rowspan=12,column=3, columnspan=13)

       
    def menu_objektu(self):
        self.objekty = Objekty.objekty
        self.volba = self.seznam_objektu.get()
        for objekt in self.objekty:
            if self.volba == objekt:
                self.strana_zadani = tk.Label(root, text="Zadej délku strany 'a'", width=15)
                self.strana_zadani.grid(row=5, column=0, sticky=W)
                self.delka_zadani = ttk.Entry(root)
                self.delka_zadani.grid(row=6, column=0, sticky=W)
                if self.volba == 'obdélník':
                    self.strana_zadanib = tk.Label(root, text="Zadej délku strany 'b'", width=15)
                    self.strana_zadanib.grid(row=7, column=0, sticky=W)
                    self.delka_zadanib = ttk.Entry(root)
                    self.delka_zadanib.grid(row=8, column=0, sticky=W)
                elif self.volba == 'úhelník':
                    self.pocet_uhlu_zadani = tk.Label(root, text="Zadej počet úhlů", width=15)
                    self.pocet_uhlu_zadani.grid(row=7, column=0, sticky=W)
                    self.pocet_uhlu_uz = ttk.Entry(root)
                    self.pocet_uhlu_uz.grid(row=8, column=0, sticky=W)

                self.button_potvrdstranu  = ttk.Button(root, text = "Potvrdit", command = self.draw_confirmed )
                self.button_potvrdstranu.grid(row=10, column=0, sticky=W)
            else:
                pass
            #self.strana_a = self.delka_zadani.get()
            
          
        

    def draw_confirmed(self):
        self.volba = self.seznam_objektu.get()
        self.objekty = Objekty.objekty
        self.strana_a = self.delka_zadani.get()
        print(f"strana_a je {self.strana_a}")
        if self.volba == 'obdélník':
            self.strana_b = self.delka_zadanib.get()
            print(f"strana_b je {self.strana_b}")
        elif self.volba == 'úhelník':
            self.pocet_uhlu = self.pocet_uhlu_uz.get()
        try:
            self.strana_a = int(self.strana_a)
            if self.volba == 'obdélník':
                self.strana_b = int(self.strana_b)
            elif self.volba == 'úhelník':
                self.pocet_uhlu = int(self.pocet_uhlu)
        except ValueError:
            print("error")

        

        if self.volba == 'čtverec':
            ctverec = Ctverec(self.strana_a)
            self.platno.delete("all")
            ctverec.draw(self.platno,self.volba,self.strana_a)
        elif self.volba == 'obdélník':
            obdelnik = Obdelnik(self.strana_a, self.strana_b)
            self.platno.delete("all")
            obdelnik.draw(self.platno,self.volba,self.strana_a,self.strana_b)
        elif self.volba == 'úhelník':
            uhelnik = Uhelnik(self.strana_a, self.pocet_uhlu)
            self.platno.delete("all")
            uhelnik.draw(self.platno, self.volba, self.strana_a, self.pocet_uhlu)


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
    

