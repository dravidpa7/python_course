#tuples are immutable

def p():
    print("------------------------------------------------------------------------------------------------------")
    
l=([1,2,3],45)
print(type (l))

l[0][0]=12
print(l)
# l[1]=23
# print(l)   - shows type error

#unpacking a tuple
a,b,c=1,2,3
print (a,b,c)

t=(1,2,3,3)
s,d,f,r = t  #print t it will show tuple (1,2,3) 
print(s,d,f,r)

print(t.count(4))
print(t.count(3))
print(t.index(2))
p()
for i in t:
    print(i)
p()

print(t*2)

#tuple to list

list=list(t)
print(list)