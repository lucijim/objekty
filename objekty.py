
import turtle as t

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
            t.forward(pixel_to_cm*self.strana_a)
            t.left(90)
        t.exitonclick()

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
            t.forward(pixel_to_cm*self.strana_a)
            t.left(90)
            t.forward(pixel_to_cm*self.strana_b)
            t.left(90)
        t.exitonclick()

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
            t.forward(pixel_to_cm*self.strana_a)
            t.left(180 - (180 * (1-2/self.pocet_uhlu)))
        t.exitonclick()


#mujuhel = Uhelnik(5,6)
#mujuhel.draw()


