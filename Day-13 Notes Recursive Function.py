#return keyword:In a function if return is excuted that will be exit from the function with certain returned values
def myfunc_(n):
    return 5+ n
a=myfunc_(10)#calling function 5+10=15
c=myfunc_(15)
print(a)#print is used to display the output
print(c)

import builtins

built_function = [
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(built_function)
print(f"Total bulit-in functions {built_function}")

                              Recursive function
                                ------------------
-->Recursive function that calls itself repatedly until a specified condition is met...
syntax:
def func_name(parmater):
    if condition: base case
        return statement
    else:
        return statement
print(func_name(arguments))
