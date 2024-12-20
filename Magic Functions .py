# class Customer:
    
#     def __init__(self, name, balance=5):  
#         self.name = name
#         self.balance = balance
#         print("The init method was called")
        
#     def __str__(self):#string representation
#         return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
#     def __repr__(self):#string representation
#         return f"Customer(name={self.name}, balance={self.balance})"
    
#     # Equality check
#     def __eq__(self, other):
#         return self.balance == other.balance
    
#     # Less than comparison
#     def __lt__(self, other):
#         return self.balance < other.balance
    
#     # Less than or equal to comparison
#     def __le__(self, other):
#         return self.balance <= other.balance
    
#     # Greater than comparison
#     def __gt__(self, other):
#         return self.balance > other.balance
    
#     # Greater than or equal to comparison (already provided in the original)
#     def __ge__(self, other):
#         return self.balance >= other.balance
    
#     # Addition of balances between two Customer objects
#     def __add__(self, other):
#         return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
#     # Subtraction of balances between two Customer objects
#     def __sub__(self, other):
#         return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

# customer1 = Customer("Alice", 10)
# customer2 = Customer("Bob", 7)
# customer3 = Customer("Charlie", 10)



# # __str__ : String conversion
# print(str(customer1))  # Customer: Alice, balance: 10
# # ==print(customer1)

# # __repr__ : Developer-friendly string conversion
# print(repr(customer2))  # Customer(name=Bob, balance=7)
# # ==print(customer2)

# # __eq__ : Equality comparison
# print(customer1 == customer2)  # False (10 != 7)
# print(customer1 == customer3)  # True (10 == 10)

# # __lt__ : Less than comparison
# print(customer2 < customer1)   # True (7 < 10)
# print(customer1 < customer3)   # False (10 is not less than 10)

# # __le__ : Less than or equal to comparison
# print(customer2 <= customer1)  # True (7 <= 10)
# print(customer1 <= customer3)  # True (10 <= 10)

# # __gt__ : Greater than comparison
# print(customer1 > customer2)   # True (10 > 7)
# print(customer2 > customer3)   # False (7 is not greater than 10)

# # __ge__ : Greater than or equal to comparison
# print(customer1 >= customer2)  # True (10 >= 7)
# print(customer1 >= customer3)  # True (10 >= 10)

# # __add__ : Adding balances
# customer4 = customer1 + customer2  # Adds balances and concatenates names
# print(customer4)  # Customer: Alice & Bob, balance: 17

# # __sub__ : Subtracting balances
# customer5 = customer1 - customer2  # Subtracts balances and concatenates names
# print(customer5)  # Customer: Alice & Bob, balance: 3



class Customer:
    
    def	__init__(self, name, balance=20):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

    def __sub__(self, other): 
        return Customer("Test_Customer",self.balance - other)

c1 = Customer("Ali") 
print(c1.balance) 
print(str(c1)) # give the address in memory because we dont identify __str__

c2 = c1 + 30
c3 = c1 - 3
print(c2.balance , c3.balance)


