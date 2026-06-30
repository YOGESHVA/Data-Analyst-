#Input Formatting from user
#input:input() function is used to take input from the user...
#1,int:Example for input as integer
'''num = int(input("Enter a Number:"))
num_2 =int(input("Enter a Number:"))
print(num+num_2)

#2,String:
how = input("Enter a character:")
print(how +' '+'Hello')

#FLoat:
num = float(input("Enter a Number:"))

print(num,"It is Monthly Salary")

#list:
group_=list(map(int,input().split())) #it split used for space covert into list
print(group_)
#string
group_=list(input())
print(group_)

#tuple
group_=tuple(map(int,input().split()))
print(group_)

group_=list(input())
print(group_)

#Eval:It will format any type data
a=eval(input("ENter a Name:"))
print(type(a))'''
#
name_=input("Enter a Your name:")
age_=int(input("Enter a Your age:"))
print(name_,"your age is",age_)
print(f"{name_} your age is{age_}")#Docs format
print("My name is %s and i'm %d years old" %(name_,age_))
print("My name is".format(name),(age))



