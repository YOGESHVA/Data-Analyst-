""" --------------Functions------------
1. It is a block of code that cab reusable
2.It avoids repated line of code
2.types of functions()
1.Bulit in function
2.user defined

1.Bulit in function
eg:print(),max(),type(),min(),sum()

2.user-define
--this function starts with a keyword def()

def func_name(parameters)
        ---------
        --------
        --------
func_name(arugments)

#Eg:
def add(a,b): #function
    print(a+b) 
add(3,4)#arugments 

Types of arugments
1.Requared Arugments:or Postional Arguments
--->We have to pass same no of Arugments with that defination of the function
eg:
def add(a,b):
    print(a+b)
add(3,6) #(5,3,3)it should  be  error we should pass same no of arugments like (5,3

2.Key word Arugments:we can pass as a pair like (variable = datatype)
def add(a,b):
    print(a+b)
add(a=4,b=5)

3.Default Arugments:we can pass Default Values
num=6
num_1=5
def add(a,b):
    print(a+b)
add(a=4,b=5)

4.Variable_Length:We can pass n no of arugments and just using {*args} in the parameters will receive tuple of arguments
They have two types:1,* 2,**
1,*:They have in the form of tuple
2**:They have in the form of Dict

1,*:They have in the form of tuple
Eg:
num=6
num_1=5
num_2=4
num_4=10
def add(*a): #we can using * n  no of arugments  we can pass 
    print(a) # it will recive the in the form of tuple of arugments
add(num,num_1,num_2,num_4) #we can calling the function like this 

2**:They have in the form of Dict
def all_(**Any):
    print(Any['Age'])
all_(Name ="Yogesh",Age = 14)

"""
#it Global Variable
num=9  #it Global Variable:We can pass the function any where and it can be print 
def fun():
    print(num)
fun()

#local Variable
def fun():
    num = 9 #Local Variable:We can pass the function inside the variable only it will be print inside
    print(num)
fun()
print(num)

#How to change outside variable inside the variable
#To change Global variable by using key word (global) that can be change completely inside the function
num = 9
def fun():
    global num
    num =77
    print(num)
fun()
print(num)



