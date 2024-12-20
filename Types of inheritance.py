# #Adding properties to child class

# #parent class
# class Person():
#     def __init__(self, name, age):
#      	self.name = name
#      	self.age = age
    
#     def display(self):
#      	print(self.name, self.age)
    
# # child class
# class Student(Person):
#     def __init__(self, name, age, dob):
#      	self.dob = dob
     	
#      	super().__init__(name, age)
    
#     def displayInfo(self):
#      	print(self.name, self.age, self.dob)

# obj = Student("Menna", 20, "05-06-2004")
# obj.display()
# obj.displayInfo()


print("#####################################################")


# ## multiple inheritance

# class Base1(object):
#  	def __init__(self):
# 	    self.str1 = "Geek1"
# 	    print("Base1")


# class Base2(object):
#  	def __init__(self):
# 	    self.str2 = "Geek2"
# 	    print("Base2")


# class Derived(Base1, Base2):
#  	def __init__(self):

# 		# Calling constructors of Base1 and Base2 classes
# 		
# 	    Base1.__init__(self)
# 	    Base2.__init__(self)
# 	    print("Derived")

#  	def printStrs(self):
# 	    print(self.str1, self.str2)


# ob = Derived()
# ob.printStrs()


print("#####################################################")






# multilevel  inheritance 

class Base(object):

 	
 	def __init__(self, name):
	    self.name = name

 
 	def getName(self):
	    return self.name



class Child(Base):

 	
 	def __init__(self, name, age):
	    Base.__init__(self, name)
	    self.age = age

 	
 	def getAge(self):
	    return self.age




class GrandChild(Child):

 	
 	def __init__(self, name, age, address):
	    Child.__init__(self, name, age)
	    self.address = address

 	
 	def getAddress(self):
	    return self.address



g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

# Hierarchical Inheritance
# Multiple classes(child) inherit from a single parent class
# Parent class
class Animal:
    def speak(self):
        return "Animal speaks"

# Child class 1
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Child class 2
class Cat(Animal):
    def meow(self):
        return "Meow!"

dog = Dog()
cat = Cat()


print(dog.speak())  
print(dog.bark())   
print(cat.speak()) 
print(cat.meow())

  
print("#####################################################")

# Hybrid Inheritance 
#A combination of multiple inheritance types.
# Parent class
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal): #Hierarchical Inheritance
    def meow(self):
        return "Meow!"


class Pet(Dog, Cat): #Multiple Inheritance
    def play(self):
        return "Pet is playing!"


pet = Pet()


print(pet.speak())  
print(pet.bark())   
print(pet.meow())
print(pet.play())   

