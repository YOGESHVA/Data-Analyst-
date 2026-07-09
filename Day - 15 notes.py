#Remove Duplicates
nums=[23,23,4,5,33]
empty_=[]
def removes_(nums,empty_):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)

#Prime Number or Not
prime_=7
count =0
def prime(prime_,count):
    for i in range(1,prime_+1):
        if prime_ % i==0:
            count+=1
    if count==2:
        print("{Prime")
    else:
        print("Not prime")

prime(prime_,count)

#Count the String
some = "python is a programming language"
count=0
def counting(some,count):
    so = some.split(' ')
    for j in so:
        count+=1
    print(count)
counting(some,count)


#palidrome
some="madam"
rev=0
def palidrome(some,rev):
    so = some.split(' ')
    for j in so:
        j = rev
if rev==some:
    print("palidrome")
else:
    print("Not Palidrome")
#Count the cap,small,space
some = "Python Is a Programming Language"
cap_count=0
small_count=0
space_count=0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
            cap_count+=1
        elif j.islower():
            small_count +=1
        else:
            space_count +=1
    print(f"There total {cap_count} number cap")
    print(f"There total {small_count} number small")
    print(f"There total {cap_count} number space")
cap_small(some,cap_count,small_count,space_count)
