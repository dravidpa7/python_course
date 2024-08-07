def p():
    print("--------------------------------------------------------------------------------------------------------")
""" class is a blue print of object
it want to start with caplital letter"""

class Name:
    pass

''' obj is enitites of a class '''
honda= Name()
type(honda)

class Human:
    def __init__ (self):
        print("hello world")    #__ called as dunter dravid obj , human () class
dravid = Human()
emma = Human()
print(dravid)
print(type (dravid))
p()

class Human:
    def __init__(self ,name, age):
        self.name=name
        self.age=age
drav=Human("dravid",19)
print(drav.name)
print(drav.age)
p()

class Hero:
    power=100   #named space var
    def __init__(self, life, hp):  #life ,hp instance var
        self.life=life
        self.hp=hp
dravid=Hero(70,200)
rahim=Hero(60,180)
rahim.life=90
print(rahim.life , dravid.life , rahim.hp ,dravid.hp)
Hero.power=50  # access by only class
print(rahim.power, dravid.power)
p()


#methods

class Human:
    #constructor
    def __init__(self , name , age, hobby):
    #these are know as attribute of an obj
        self .name = name
        self.age =age
        self .hobby = hobby
    #var they belong to obj - attribute - they contain info about property or charcterstics of an obj
        
    # methods
    def greet(self):
        print(f"Hey my name is {self.name} . good morning ")
        
rahul=Human("Dravid", 19, "solve")
rahul.greet()   #instance method
print(rahul.name)   #instance var

#if you want to add one more ins var
rahul.sex="male"    #instend self.sex

print(rahul.sex)
p()

#class variable

class Human:
    # class var
    population= 0
    data =[]
    def __init__(self , name):
        self.name =name
        self.population += 1
        Human.population +=1
        Human.data.append(self.name)
rahul=Human("dravid")
emma=Human("emma")
print("Human.population",Human.population)
print("rahul.population",rahul.population)
print("emma.population",emma.population)
print("Human.data",Human.data)
p()

class Drav:
    pop=0
    def __init__(self , name ,alive=True ):
        self.name=name
        Drav.pop+=1
        
    def dead (self):
        if self.alive :
            print(self.name , "no ")
            self.alive=False
        else:
            print("dead")
dravid=Drav("Rahul")
emma=Drav("emma")
bob=Drav("bob")
print("Drav.pop",Drav.pop)
p()

#inheritance

#add attribute in derived class
class Human:
    # class var
    population= 0
    data =[]
    def __init__(self , name):
        self.name =name
        self.population += 1
        Human.population +=1
        Human.data.append(self.name)
rahul=Human("dravid")
emma=Human("emma")
print("Human.population",Human.population)
print("rahul.population",rahul.population)
print("emma.population",emma.population)
print("Human.data",Human.data)
#Human base class employee derved class
class Empolyee(Human):
    #re intiate constructor
    def __init__(self , name, company ,post):
        super().__init__(name)
        
        #attribute employee class
        self.company=company
        self.post=post
        
#add method in derived class
    def hire(self, person):
        print(f"{person} has been hired in a company")
        Human.data.append(person)
        
dravid=Empolyee("Dravid","sync","Dev")
print(dravid.post)
dravid.hire("selva")
print("Human.data",Human.data)
p()

#polymorphism means many forms
# two types of poly morphism : functional polymorphism , operator level polymorphism
#one oprator doing diffrent kind of operation

# operator level polymorphism
print(2+2)
print("2"+"2")
print("a"*3)

#functional polymorphism
l=[1,2,3]
print(len(l))
print(sum(l))

def mul(*args):
    total=0
    for i in args:
        total += i
    print(total)
mul(1,2,3,4,5 )