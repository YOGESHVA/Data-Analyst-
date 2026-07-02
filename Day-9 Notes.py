""" Loops
1,for loop:A for loop is used to itterate over a squence, list,tuple
any_="python is a language"
any_="python is a language"
for j in any_:
    print(j)
any_=[1,2,4,5]
for j in any_:
    if j%2==0:
        print("Even",j)

any_ =(1,2,3,4)
for a in any_:  #a is called instance varible
    print(a)

for j in any_:
    print(j)

any_ ={"Name":"Teja","Role" : "student"}
for key in any_.keys():
       print(key)

-->else in for loop:The else bock will be excuted after the for loop but in case the loop is breaked then it will never entered in the else block

any_ =[1,2,3,4,5]
for i in any_:
       print(i)
else:
    print("Program Ended")

                                            Control Statments

1.break:The break statments is used exit from the loop
any_ =[1,2,3,4,5]
for i in any_:
    print(i)
    if i==3:
           break
else:
    print("Program Ended")

2.contiune:The comtinue will skip the current itteration
any_ =[1,2,3,4,5]
for i in any_:
    if i==3:
        continue
    print(i)
else:
    print("Program Ended")
3.pass:space holder
any_ =[1,2,3,4,5]
for i in any_:
    if i==3:
        break
    print(i)
else:
    pass


4,Range():It is in bulit function that is used to generate a squence upto a limit

syn:range(starting_value,ending_value,step)

for i in range(1,10):
    print(i)
for i in range(2,11):
    if i%2==0:
        print(i)






2,while loop:The while loop will excute untill the condition becomes true 
eg:
i=1
while i<5:
    print(i)
    i+=1
eg:It will runs iterate upto we stop
i=1
while i<5:
    print(i)

3,assert
-->It will used to check the condtion,but it will raise an error incase it is false
num=int(input("Enter a NUmhber:"))
assert num >= 18,  "Your Age must be 18 years"

i=1
while i<5:
    print(i)
    i+=1

"""
#Generate 100
#while loops two examples
#for loops only even 
"""for i in range(0,100,2):
    print(i)"""
#
for i in range(1,11):
    if i%1==0:
        print(i)
    
