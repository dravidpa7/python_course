def p():
    print ("---------------------------------------------------------------------------------------------------")
    
d={}
print (type (d))

f=dict()
print(f,type(f))

z={
    "apple":12,
    "mango":15
}
print(z)

#creating dict using zip method
p()

k=["a", "b",'c']
v=[1,2,3]

r=dict(zip(k,v)) ##vv , kk, vk , kv accepted 
print(r)

print(len(r))

key=[1,2,3,4]
value=["a",'a','f','d']
g=dict(zip(key,value))
print(g)                 #duplicates are not allowed only in keys duplicates are allowed in values 
print(len(g))
print(g.get(1))

#access dict

print(r["a"]) # r[5] key error


p()
#to avoid error then we can use get method
print(r.get("a"))
print(r.get("g"))
#instend we can use

print(r.get("g", "not available"))

print(r.get("g", 0))
p()

#updateing existing values in dict
g[1]="tea"
print(g)
g[1]={"tea"}
print(g)
g[1]={"tea":10,"coffee":20}
print(g)

#update new element
g[5]="hi"
print(g)

#updete dict using new dict
new ={6:'k',7:'l',8:'m'}
g.update(new)
print (g)
p()

#delete  data from dict
#citizenship check

print(1 in g)
print(13 in g) # 1 key present in G

#use pop() function to delete selected item in dict

print(g)
print("poped element ---->", g.pop(1))
print(g)
#use ppop item function to delete last item from the dict
print ("pop item () func to delete last item --->",g.popitem())
print (g)

#we want to delete whole dict use del () func

del g

# print(g)  output will be NameError: name 'g' is not defined
p()

#iterate dict
for i in r:
    print(i , r[i])
print('another method')
for i,j in r.items():
    print(i,j)
    
print(r.items())
p()
#more dict methods

print(r.keys())
print(r.values())
print(r.items())
p()

name ={1,2,3,4,1,2,3}
rep={}
for i in name:
    if i not in rep:
        rep[i]=1
    else:
        
        rep[i] +=1
        
print(rep)