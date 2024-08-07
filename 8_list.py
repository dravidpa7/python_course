def p():
    print("------------------------------------------------------------------------------------------------------")

#data structures in python
#list
#tuples
#dictionaries
#sets
    
#creation of list
l=list ()
print (type(l))
l=[]
print (type(l))
l=[1,2,3,4,5,6]
print(l)
print(id (l))
l[0]=0
print(l)
print(id (l) )  #both id are remains same
p()

#list slicing same as string slicing

a=[1,2,3,4,5,6]
c=len(a)
print(c)
print (a[0:5:2])
print (a[2:c])   # here we are using size to set the last ele
print (a[:])
print (a[::-1])
print (a[1:-2:1])  # last value n-1
print (a[0:6])
print (a[-1:-(c+1):-1])  # the value len will be 7 ,  neg index add -1 , pos index sub -1
p()


#list inbuilt functions
l=[1,2,3,4,5,6,7,6,6,6]
a=l.count(6)
print(a)
print(l.index(7))
l.pop(7)    #in pop we give only  index pos
l.pop()
l.pop()     #delete last ele of list
print(l)
l.remove(6)
print(l)
x=(3%2) +(4//2)
print (x)
#floor divison round the quatient