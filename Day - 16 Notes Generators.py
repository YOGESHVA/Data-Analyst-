"""--------------------------Generators---------------
--> This generators is special function that returns the iterator. instead of returning all the values at once
-->Here we are  going to used yield keyword

def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
#print(next(so))

# Working of Generators
--> When a function is called
-->It does not excute the function immediately
-->It will returns the generate object
-->Then the function will pauses at each yield
--> When the next() is called again excution resumes from where it stoped
def demo():
    print("start")
    yield 1

    print('Middle')
    yield 2

    print('Third')
    yield 3
how=demo()
print(next(how))
print(next(how))
print(next(how))

def how(so):
    for i in range(so):
        yield i * 1
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
def how(so):
    for i in range(so):
        print (i * 1)
how(5)


--------------------------Differnece
Function:
-->return
-->Return complete result
-->Function will end after the return the values
-->More memory usage
-->This function never resume # it print automatically

Generator
-->yield
-->Return one value
-->Pauses after every yiled
-->Less Memory usage (if you want how many we can allocate)
-->Resumes after next()

#Yield Keyword
-->This will produces the value
-->But the yield pauses the function
-->And yield will save the function current state
-->yield will continues where it stoped
 next() keyword
 ----------------
-->The  next() function is used to retrieve the next value from a generator
Stop iteration
-->Calling function after all values retrieve then it will raise error and stopIteration exception
Ex:

def even(num):
    for i in range(num):
        if i % 2 ==0:
            yield "even"
        else:
            yield "odd"
how=even(33)
print(next(how))"""

#Generator expression
#-->The generator expression is similar to a list comprehension but uses parenthesis() instead of []
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))










        

