def p():
    print("-----------------------------------------------------------------------------------------------------------------")
    
a= int (input ("enter the age of a person : "))

if a>18:
    if a>65:
        print("take rest")
    else:
        print("eligible ")

else:
    print ("not eligible")
    
p()


n=int (input ("check the whether the no is pos or neg or neautral : "))

if n<0:
    print ("positive")
    
elif n>0:
    print ("negative")
    
else:
    print ("neautral or equal to zero")
    
p()

l=[1,2,3,4,5,10,6]
high=l[0]
for i in l:
    if i > high:
        high=i
print(high)

print(min(l))
print(max(l))
p()

#grading system

g = int (input ("enter the mark : "))

if g>90:
    print ("o grade")
elif g<=90 and g>80:
    print ("a + grade")
elif g<=80 and g>70:
    print("a grade")
else:
    print("below a grade")
    
p()