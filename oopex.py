class Bikes:
    def __init__(self, brandname,year):
        self.brandname = brandname
        self.year = year
    
    def topspeed(self, topspeed):
        return f'{self.brandname} topspeed is {self.year}'
    
    def type(self):
        return f'{self.brandname} is geared bike'
    

bike1 = Bikes('BMW', 220)
print(bike1.topspeed(220))
print(bike1.type())
bike2 = Bikes('Jaguar', 250)
print(bike2.topspeed(250))
print(bike2.type())



class Animal:
    def sound(self):
        print('Animal making sound')

class Cat(Animal):
    def meow(self):
        print('Cat meows')

class CatChild(Cat):
    def eat(self):
        print('Eats bread')


a = CatChild()
a.meow()
a.sound()
a.eat()