"""
----------------------------Modules--------------------------------------
--> A Module is a python file (.py) that contains reusable code
1.Varibles
2.Functions
3.Classes
4.Objects
5.Statements

Why this
--------
-->Insead of writing the same code repatedly, we can store it in a module
and use it whenever needed
Types of Modules
1.user- define
import module
print(module.add(5,3))
print(module.sub(5,3))

from module import add,sub
print(add(5,3))
print(sub(5,3))

from module import * #from :specific character 
print(sub(5,3))
print(add(5,3))

import  module as m
print(m.add(5,3))
-->import math
-->print(math.sqrt(25))
-->print(math.factorial(5))
-->print(math.pow(2,5))
-->print(math.pi)
-->print(math.ceil(4.1))
sqrt() ---> square root
factorial--> factorial
pow()--->power
ceil-->roundup
pi-->pi value
2.Bulit-in
-->math
-->os
-->sys
-->random

import specific function

"""
import os
print(os.getcwd()) # current diractory
os.mkdir("Teja") #It creates a new folder commuciate the system
os.rmdir("Teja") # it removes 

#sys:This will give inforamation about python interpetr
import sys
print(sys.version)

#random :It used to generate random values
import random
print(random.randint(2000,9000))

colors = ["Yellow","Red","Blue","Green"]
print(random.choice(colors))













