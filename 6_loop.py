def p():
    print("-----------------------------------------------------------------------------------------------------------------")
#while loop

i=0
while i<6:
    print ("you are the best")
    i+=1     # in python there is no special syntax like i++ , i--

i=1
while i<=10:
    print (i ,end=" ")
    i+=1 
print(" ")
p()
    
i=1
s=0
while i<=10:
    s=s+i 
    print (i ,end=" ")
    i+=1
    
print(s)

#range

l=[*range(5,10)]
print(l)



# looping for tables 
for i in range (1,11):
  print (i,"* 5 =", i*5)
p()


n=int (input("enter the value : "))

for i in range (n):               
    for j in range (n):
        print ("@",end="")           
    print(" ")


"""
output :
enter the value : 5
@@@@@ 
@@@@@ 
@@@@@ 
@@@@@
@@@@@

"""

f= int (input ("enter the value : "))

for i in range (1,f+1):
    for j in range(i):
        print ("#" , end=" ")
    print (" ")
    
"""
enter the value : 3
#  
# #  
# # #

"""
a=[1,2,3,4,5,6,7,8]
for i in a:
    pass

for i in a:
    if i==5:
        continue
    if i==7:
        break
    print(i)