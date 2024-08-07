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



