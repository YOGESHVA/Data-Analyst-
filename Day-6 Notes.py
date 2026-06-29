# Type converation:This is process of converting one data type into another
#int:string:float
num=8.9
how=str(num)
print(how)
print(type(how))
num_2=int(num)
print(num_2)

#Float: string,integer
num=8.9
how=str(num)
print(how)
print(type(how))
num_2=int(num)
print(num_2)
#string:Integer:Float;List:tuple
#string into integer
hai='38' # we can convert the string into interger but it only digits not names
num=int(hai)
print(num+10)
#string into Float
hello='67.8'
num=float(hello) # we we can convert the string into float but it only digits not names
print(num+10)
#string into List
any_="12345"
x=list(any_)
print(x)

#string into tuple
any="12345"
x=tuple(any)
print(x)


#list:String,Tuple,Dictonary
#list into string
var=['p','y','t','h','o','n']#by using join method we not do in by using string it will come brackets
text="".join(var)
print(text)

#list into tuple
var=['p','y','t','h','o','n']
var_1=[10,20,30]
text=tuple(var)
text_2=tuple(var_1)
print(text)
print(text_2)
#list into Dictonary
pyth_=[('a',1),('b',2)] 
conve=dict(pyth_)
print(conve)

#Tuple:string,list
#Tuple into list
fam=(1,2,3,4)
v=list(fam)
print(v)
#Tuple into string
fam=('y','o','g','e','s','h')
v=''.join(fam) # By using same as join method
print(v)

#Bulit in functions
#---------------
#str()
#float()
#int()
#list()
#tuple()
#dict()

