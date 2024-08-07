def p():
    print ("---------------------------------------------------------------------------------------------------")

s=set()
print(type (s))
s={1,2,3,4,5,2,1,3,3,2,1} # it does  not contain repeated value
print(s)

s=set("rahul")
print(s)

for i in s:
    print(i)
p()

#update and delete  value in the set
a=set({2,3,4,2,1,5})
a.add(6)
print(a)

new="dravid"
a.update(new)
print(a)
a.pop()
print(a)
a.remove(6)
print(a)
p()
#union and intersection
a={1,2,3,5,6}
b={8,9,6,7,5}

print(a.intersection(b))
print(a.intersection(a)) #all ele are common
print(a.union(b))
print(a.difference(b)) # a only intersection will be omited
p()

d="what is your name and what is your age"
l=d.split()
print(l)
print(set(l))