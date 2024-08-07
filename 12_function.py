def p():   #called func
    
    print("-----------------------------------------------------------------------------------------------------------------")
#user defined func and builtin func
    
#calling func
p()

# Doc string to provide a additional information

# Doc string greet()
''' hi hello'''
def greet(name):
    print ("Hi i am ", name)
    
greet("Dravid")
greet("indujan")

p()
 
d=1+3
print(type(print(d)))  # print inside argument are non type

def add(a,b):
    c=a+b
    print(c)    
    
c=add(2,3)#it is outside the func so it return none
print(type(c))

p()
def add(a,b):
    c=a+b
    return(c)

d=add(1,4)
print(d)
print(type(d))


def intr(name , age , hobby):
    return name , age , hobby

a,b,c=intr(1,2,3)
print(a, b , c)   # they are stored data in tuple form we can use single element to print multiple element

#scope local and global

a=10
def g():
    global x
    x=5
    print(x)
g()
print (a)
print(x)
p()

#lambda function
def add(a,b):
    c=a+b
    return c
print(add(7,3))

#procedure -> lambda parameter : return
print((lambda a,b,c : a+b+c)(1,2,5))
e=(lambda a,b,c : a+b+c)
print(type (e))
print(type (g))

#check greater value in two elements
def greter(a,b):
    if a>b:
        return a
    else :
        return b
c=greter(34,5)
print(c)

#using lambda
print((lambda a,b : a if a > b else b)(34,5))
p()

def even(num):
    for i  in num: 
        if i % 2 == 0 :
            print(i)
inp=[1,2,3,4,5,6,7]
even(inp)
p()

#print unique no
#here x and n is parameter
def rep(x,n):
    for i in lis:
        if i not in n:
            n.append(i)
    print(n)
            
lis=[1,2,3,4,1,2,3]
new=[]
#here lis and  new actual value is argument
rep(lis,new)

#positonal argument
#the value you pass when calling func are matched according to the position

def arg(x,y):
    print(x,y)
    
arg(1,2)       #arg(1) TypeError: arg() missing 1 required positional argument: 'y'

p()
#default argument is y =dravid non default argument always be at the first
def nun(x,y="dravid"):
    print(x,y)
    
nun(1)
nun(1,2)
p()

#arbitary argument - tuple format
def test(*args):
    print(type(args))
    for i in args:
        print(i)
        
test(1,2,3,"dravid",12.1)

p()
#keyword argument
def test(**args):
    print(type(args))
    print(args)
    for k,v in args.items():
        print(k,v, sep=" : ")
        
test(a1="a",b1="b")
p()

#mix
def mix(a,b,c,age=45,*args,**dic):
    print(a,b,c)
    print(age)
    print(args)
    print(dic)
    
mix(1,2,3,67,2,3,4,name="dravid", ag="18")
