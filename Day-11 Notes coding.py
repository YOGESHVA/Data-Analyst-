#palidrome
"""so =input("Enter a word:")
empt_ = ""
for i in so:
    empt_ = i + empt_
if empt_==so:
    print(f"{so} Palidrome")
else:
    print(f"{so} Not Palidrome")

so =input("Enter a word:")
ok=so[::-1]
print(ok)
if ok == so:
    print("Palidrome")
else:
    print("Not palidrome")

#Fibonacci series
num = 0
num_2 = 1
limit_=int(input("Enter a Number: "))
print(num,num_2,end=" ")
for i in range(1,limit_+1):
    all_num = num + num_2
    num = num_2             
    num_2 = all_num
    print(all_num,end=" ")
    print()
#Calculator
val_1=int(input("Enter a Number:"))
val_2=int(input("Enter a Number:"))
user_in=int(input("enter \n1.add: \n2.sub: \n3.mul: \n4.pow: \n5.division: ")) #\:next line
if user_in == 1:
    print(val_1 + val_2)
elif user_in == 2:
    print(val_1 - val_2)
elif user_in == 3:
    print(val_1 * val_2)
elif user_in == 4:
    print(val_1 ** val_2)
else:
    print(val_1 // val_2)

#Table
val_1=int(input("Enter a Number:"))
for i in range(1,11):
    print(f"{val_1} x {i} ={val_1 * i}")"""

#Perfect Number:6:1+2+3=6 factors of 6 and they add 1,2,3=1+2+3=6
num = int(input("Enter a Number:"))
sum_=0
for i in range(1,num):
    if num % i == 0:
        sum_+=i
if sum_ == num:
    print(f"{num} it is perfect number")
else:
    print(f"{num} it is not perfect number")

#Bank Account
Details = {"Name":"Yogesh",
        "Atm PIn":"2200",
        "Balance":50000}
print("----Welcome to the Atm ------")
user_in = input("Enter your Atm Pin:")
user_in_=int(input("enter \n1.Withdraw: \n2.Deposite: \n3.Pinchage:"))
if len(user_in)==4:
    if user_in == Details["Atm PIn"]:
        if user_in_ == user_in:
            print(user_in_)
            
        #Amount = int(input("Enter a Your Amount:"))
        
            
        #else:
            
            
            
    else:
        print("Enter a correct pin")
else:
    print("Incorrect pin")

    



    
        
    
    




    

    
