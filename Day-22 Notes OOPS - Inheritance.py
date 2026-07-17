"""
Inheritance
-----------
It is an oop concept where one class (child/derived) acquired the properties and methods
of another class (parent/Base)
class parent:
    pass
class child (parent):
    pass

1.Single Inheritance
--------------------
A child class inherits from one parent is Single Inheritance
"""
class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def barks(self):
        print("Dog Barks")
class cat(dog):
    def skils(self):
        print("Meow")
d=cat()
d.skils()
d.barks()
d.sound()

class father:
    def land(self):
        print("5 ar of land")
class son(father):
    def flat(self):
        print("3BHK ")
s=son()
s.land()
s.flat()

#Multiple Inheritance:A child inherits more than one parent is called
class father:
    def skills(self):
        print("Driving")
class mother:
    def talent(self):
        print("Cooking")
class son(father,mother):
    def mine(self):
        print("coding")
all_ = son()
all_.skills()
all_.talent()
all_.mine()

class father:
    def skills(self):
        print("Driving")
class mother:
    def talent(self):
        print("Cooking")
class sister:
    def learn(self):
        print("Python")
        
class son(father,mother,sister):
    def mine(self):
        print("coding")
all_ = son()
all_.skills()
all_.talent()
all_.learn()
all_.mine()

#Multi Level
#One child class becomes the parent for another class
class grandfather:
    def house(self):
        print("Owns House")
class father(grandfather):
    def flat(self):
        print("New 3BHK flat")
class son(father):
    def car(self):
        print("Have a Car")
fam = son()
fam.house()
fam.flat()
fam.car()




"""class grandfather:
    def house(self):
        print("Owns House")
class father:
    def flat(self):
        print("New 3BHK flat")
class son(father):
    def car(self):
        print("Have a Car")
class child("""

#Hierarchical
#-->Multiple childs inherits from the same parent
class mother:
    def gold(self):
        print("10 KG gold")
class pinky(mother):
    def show(self):
        print("Will get 5 Kg gold")
class yuktha(mother):
    def show_2(self):
        print("Will get remaining 5 Kg gold")
child_1=pinky()
child_2=yuktha()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()




class father:
    def gold(self):
        print("10 KG gold")
class son_1(father):
    def show(self):
        print("Will get 5 Kg gold")
class son_2(father):
    def show_2(self):
        print("Will get remaining 5 Kg gold")
class son_3(father):
    def show_3(self):
        print("Will get 10 kg gold")

child_1=son_1()
child_2=son_2()
child_3=son_3()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()

child_3.gold()
child_3.show_3()


#Hybrid inheritance
#-->This is the combnation of two or more types of inheritance
#Example of Mutiple + Multiple-level
class A:
    def methodA(self):
        print("Class A")
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')
so = D()
so.methodA()
so.methodB()
so.methodC()

#Super Method:This super() function is used to access the parent class methods or constructor in the child class...
class parent:
    def show(self):
        print('Parent Methods')
class chile(parent):
    def show(self):
        super().show()
        print('child class')
chi_=chile()
chi_.show()


class parent:
    def show1(self):
        print('Parent Method')
class child_1(parent):
    def show2(self):
        print('Child Class')
class child_2(child_1):
    def show(self):
        super().show1()
        super().show2()
        print('Parent Class')
chi=child_2()
chi.show()

class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Teja',101)
an.display()




    
