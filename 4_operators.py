def p():
    print("--------------------------------------------------------------------------------------------------")
    
""""
operators

add
sub
mul
div
mod%
floor
pow
"""

a=5
b=3
print(a+b)
print(a%b)    #mod
print(a//b)	  #floor  i gives only nearest smaller integer left side of no line 
print(a**b)   #pow
p()

a="hello "
b="world"
print(a+b)
print(a*3)
p()

#comparison operator for alphabets

# a="hello "
# b="hello " exceptional case you can try  this both are  equal

print(a==b)
print(a<=b)     #by using lexographical order
print(a>=b)
print(a!=b)
p()


# compound assignment operator
a=4
a+=1
print (a)

#logical operator
a=3
b=5
print(a and b) # and operator will show only the greater value
print(a or b) #or operator will show only the small value
print(not b)
p()


#membership operator

a="dravid kamando"
k="da"
print( k in a)   #if we store seprate string in a single var it will check the whole string
print("d" in a)
p()

#is operator
a=5
c=6
b=5

print(id (a),id(c), id (b))

