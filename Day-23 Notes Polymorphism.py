"""
Polymorphism
--->It means many forms
--->It allows same method,function or operator to perform different tasks depending on the same object
types:
Method overloading
-----------------
-->Method overlodaing means have multiple methods with the same name but different parameters
2.Method Overiding
3.operator overloading

class Cal:
    def add(self,num,num_2=5):
        print(num+num_2)
    def add(self,num,num_2=0,num_3=3):
        print(num+num_2+num_3)
obj=Cal()
obj.add(45)
obj.add(2,3)

def add(a,b):
    print(a+b)
add(5,3)
add('p','q')#one method in diffrent forms single form like tupple stringand any method
add([5,7],[7,3])

2.Method Overr
------------------
-->The method overriding occurs when a child provides its own implementation of a method already defined in its
parent class...
class animal:
    def sound(self):
        print("Animals makes sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d=dog()
d.sound()

3.Operator Overloading
-------------------
-->This allows operators (+,-) to work differently for user-defined objects
-->1.__add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5._eq_() ==
6.__it__() (<)



class student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks + other.marks
s1= student(1)
s2=student(5)
print(s1 + s2)


        
class student:
    def __init__(self,marks):
        self.marks=marks
    def __sub__(self,other):
        return self.marks - other.marks
s1= student(1)
s2=student(5)
print(s1 - s2)

class student:
    def __init__(self,marks):
        self.marks=marks
    def __mul__(self,other):
        return self.marks  * other.marks
s1= student(1)
s2=student(5)
print(s1 * s2)

class student:
    def __init__(self,marks):
        self.marks=marks
    def __truediv__(self,other):
        return self.marks / other.marks
s1= student(1)
s2=student(5)
print(s1 / s2)

Data Absrtaction
----------------
-->Data Abstaction IS THE process of hiding implementation details and showing only the essentail data to the user
Eg:
---ATm
---CAR
---APP

"""
from abc import ABC, abstractmethod
class bank:

    @abstractmethod
    def interest(self):
        raise NotImplementedError('Subclass must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI Interest Rate: 6.5 %')
class HDFC(bank):
    def interest(self):
        print('HDFC Interest Rate: 5.5 %')
class ICIC(bank):
    def interest(self):
        print('ICIC Interest Rate: 6.9%')
banks = [SBI(),HDFC(),ICIC()]

for j in banks:
    j.interest()









