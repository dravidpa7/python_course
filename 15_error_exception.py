def p():
    print ("---------------------------------------------------------------------------------------------------")


print(dir(__builtins__))
#these are some errors in python

#Try - this block handlesthe error in your code if any it exit''
#except- this block gives the output that your want to show if your code fault

a=2
b=0

try:
    print(a/b)
except Exception as e:
    print("Check your code broo !!!!!!!!",chr(128513), e)
print(" The process is completed!!!")
p()



a=20
b=0
try:
    print("open file")
    print(a/b)
    print("close file") # this will not work here
    
except Exception as e:
    print("The error is ",e)
p()


a=20
b=2
try:
    print("open file")
    print(a/b)
    
except Exception as e:
    print("The error is ",e)
    print("close file") # this will not work here
p()

#we can use
a=20
b=2
try:
    print("open file")
    print(a/b)
    
except Exception as e:
    print("The error is ",e)
    
finally:
    print("close file") 
p()

    
    