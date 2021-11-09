
import turtle 
import objekty_gui

pixel_to_cm = 37.8


class Ctverec:
    def __init__(self,strana_a):
        self.strana_a = strana_a

    def obvod(self):
        return 4*self.strana_a
    
    def obsah(self):
        return self.strana_a**2

    def draw(self):
        for ii in range (4):
            turtle.forward(pixel_to_cm*self.strana_a)
            turtle.left(90)
        turtle.exitonclick()

class Obdelnik:
    def __init__(self,strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        return 2*self.strana_a*self.strana_b
    
    def obsah(self):
        return self.strana_a*self.strana_b

    def draw(self):

        for ii in range (2):
            turtle.forward(pixel_to_cm*self.strana_a)
            turtle.left(90)
            turtle.forward(pixel_to_cm*self.strana_b)
            turtle.left(90)
        turtle.exitonclick()

class Uhelnik:
    def __init__(self,strana_a,pocet_uhlu, polomer_vepsane=0):
        self.strana_a = strana_a
        self.pocet_uhlu = pocet_uhlu
        self.polomer_vepsane = polomer_vepsane

    def obvod(self):
        return self.strana_a*self.pocet_uhlu

    def obsah(self):
        return 1/2*self.strana_a*self.pocet_uhlu*self.polomer_vepsane

    def draw(self):
        for ii in range (self.pocet_uhlu):
            turtle.forward(pixel_to_cm*self.strana_a)
            turtle.left(180 - (180 * (1-2/self.pocet_uhlu)))
        turtle.exitonclick()


#mujuhel = Uhelnik(5,6)
#mujuhel.draw()


