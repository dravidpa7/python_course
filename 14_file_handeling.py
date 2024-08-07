#text and binary file
def p():   #called func
    
    print("-----------------------------------------------------------------------------------------------------------------")

"""    r - read only , w - write only , a - append only , wt - write text , wb - write binary , rb - read binary , rt - read text"""

f=open ("name.txt")
print(type (f))
print(f.closed)
print(f.read())
f.close()
print(f.closed)
p()

f = open ("name.txt" ,"w")
f.write("i am writable now !")
f.close()

f=open ("name.txt")
print(f.read())
p()

#with open in read format
with open("name.txt") as f:
    print (f.read())
print(f.closed)
p()

#with open in write format
with open("name.txt", "w") as f:
    print (f.write("Hey , I will able to write in this file")) # 39 is the length of the string 
print(f.closed)
p()

#reading data from file
with open("new.txt", "r") as f:
    data=f.read(10)
    print(data)
    # the pointer placing the last pos
    print(f.tell())
    data=f.read(13)
    print(data)
    print(f.tell())
    # by using tell method to find the the pointer pos
    data=f.read(10)
    print(data)
    data=f.read(10)
    print(data)
    print("   ")
    
    # by using seek method to reset your file pos
    
    f.seek(2)
    f.tell()
    print(f.read())
    print(" ")
    
    # read lines
    f.seek(0)
    data = f.readline()
    print(data)
    print(f.readline())
    print(f.readline())
print(f.closed)
p()



with open("dravid.jpg", "rb") as f:
    data = f.read()
    print(data)
    
    with open("new.jpg", "wb")  as i:
        i.write(data)
        print(data)
p()


#append
with open("name.txt", "a") as j:
    j.write(" the content has been appended")
    
with open("name.txt", "r") as c:
    print(c.read())
    
    