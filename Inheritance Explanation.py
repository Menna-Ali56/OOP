##### Inheritance Explanation

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# class Person(object):

#  	# Constructor
#  	def __init__(self, name):
# 	    self.name = name

#  	# To get name
#  	def getName(self):
# 	    return self.name

#  	# To check if this person is an employee
#  	def isEmployee(self):
# 	    return False


# # Inherited or Subclass 
# class Employee(Person):

#  	# Here we return true
#  	def isEmployee(self):
# 	    return True



# person = Person("Ahmed") # An Object of Person
# print(person.getName(), person.isEmployee())

# emp = Employee("Ali") # An Object of Employee
# print(emp.getName(), emp.isEmployee())



print("############################################################")


# Python code to demonstrate how parent constructors
# are called.

# parent class
# class Person(object):

#  	# __init__ is known as the constructor
#  	def __init__(self, name, idnumber):
# 	    self.name = name
# 	    self.idnumber = idnumber

#  	def display(self):
# 	    print(self.name)
# 	    print(self.idnumber)

# # child class
# class Employee(Person):
#  	def __init__(self, name, idnumber, salary, post):
# 	    self.salary = salary
# 	    self.post = post

# 		
# 	    Person.__init__(self, name, idnumber) 
#         #it's equal super()__init__(name,idnumber)


# a = Employee('Rahul', 886012, 200000, "Intern")

# a.display()


print("########################################################")

# Python code to demonstrate how to use super()

# parent class
class Person():
    def __init__(self, name, age):
    	self.name = name
    	self.age = age
    
    def display(self):
    	print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
    	self.sName = name
    	self.sAge = age
    	# inheriting the properties of parent class
    	super().__init__("Osama", age)
    
    def displayInfo(self):
    	print(self.sName, self.sAge)

obj = Student("Khalid", 23)
obj.display()
obj.displayInfo()
