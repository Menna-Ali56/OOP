# ##Constructors explanations
# class Customer:
#     def __init__(self, name, balance):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")

# cust = Customer("Lara de Silva" , 100)
# print(cust.name) # <-- attribute is created anyway
# print(cust.balance) # <-- attribute is created anyway


##Constructors with default values

# class Customer:
#     def	__init__(self, name, balance=0):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")
        

# cust = Customer("Lara de Silva") 
# print(cust.balance) # <-- attribute is created anyway

###Constructors Vs. Destructors

class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj  # the object is removed

