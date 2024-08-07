def p():
    print("----------------------------------------------------------------------------------------")

print("dravid"=="divard")
# A= 65 , Z = 90 , a=97,z=122 -ascii
#ord used for encoding 
print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))
p()

#chr
print(chr(97))
print(chr(98))
print(chr(2325))  #a b क ख ग 🙘 🚀 😀
print(chr(2326))
print(chr(2327))
print(chr(128600))
print(chr(128640))
print(chr(128512))
p()

a="dravid"
print (a[0])
c=len (a) ; print (c , end=" ")
print (a[-c])  # length is 6 and the output will be -6 neg index

#slicing string
print (a[0:5:2])
print (a[2:c])   #here we are using size to set the last ele
print (a[:])
print (a[::-1])
print (a[1:-2:1])  # last value n-1
print (a[0:6])
print (a[-1:-(c+1):-1])  # the value len will be 7 ,  neg index add 1 , pos index sub -1
p()

#string methods
#capitalize , title ,upper ,lower , find , count , index , replace ,split ,islower , isupper,isnumeric , isalpha
b="my name is dravid"
print (b.capitalize())  # first only capital
print (b.title())		# all  letter first letter will be capital
print (a.upper(), a.lower() , b.find("f"))     # in find given ele not present in string return -1
print (b.count("a"),b.index("d"))              # in index given ele not present in string return error ele not pre
print (a.replace ("d", "a"))
print (a.split("a"))
print (b.islower())  ; print("adr12".isalpha numeric())

#string formating

name=input()
age =input()
print ("hey my name is",name ," my age is",age)

#to over come this style we are using string formting

print("hey my name is {}  my age is {}".format(name,age))   #this is only in py 3.6 above version only

#more advance string format

print(f"hey my name is {name}  my age is {age}")
p()

#string concantenation

a="dra"
b="vid "
print (a+b)
print ((a+b)*3)
p()

c ="the quick brown fox jumps over the lazy dog"
for i in c:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print (i , end =" ")
p()

#palindrome
n=str(input("enter the string : "))
a="".join(reversed(n)) 
print(a)
a=n[::-1]
print(a)
if (n==a):
    print ("palindrome")
else :
    print ("not palindrome")