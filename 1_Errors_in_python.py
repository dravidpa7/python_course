print "hello"  #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?

l=[1,2,3]
print(l[5])    #IndexError: list index out of range

import rahul   #ModuleNotFoundError: No module named 'rahul'


d={1:3,2:4}   
print(d[6])    #KeyError: 6


from math import cube #ImportError: cannot import name 'cube' from 'math' (unknown location)


it=iter([1,3])
print(next(it))
print(next(it))
print(next(it))   #StopIteration


print("2"+2)   #TypeError: can only concatenate str (not "int") to str



int("wae")  #ValueError: invalid literal for int() with base 10: 'wae'


print(dra)   #NameError: name 'dra' is not defined



print(x=100/0) #ZeroDivisionError: division by zero

