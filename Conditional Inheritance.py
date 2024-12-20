##Conditional Inheritance in Python
class A(): 
 	def __init__(self, x): 
	    self.x = x 
 	
 	def getX(self): 
	    return self.X 
 	
class B(): 
 	def __init__(self, x, y): 
	    self.x = x 
	    self.y = y 
 	def getSum(self): 
	    return self.X + self.y 

class C_A(A): 
 	def isA(self): 
	    return True
 	
 	def isB(self): 
	    return False



class C_B(B): 
 	def isA(self): 
	    return False
 	
 	def isB(self): 
	    return True

# return required Object of C based on cond 
def getC(cond): 
 	if cond: 
	    return C_A(1) 
 	else: 
	    return C_B(1,2) 

# Object of C_A 
ca = getC(True) 
print(ca.isA()) 
print(ca.isB()) 
 	
# Object of C_B 
cb = getC(False) 
print(cb.isA()) 
print(cb.isB()) 


# class A(object): 
# 	def __init__(self, x): 
# 		self.x = x 
# 	
# 	def getX(self): 
# 		return self.X 

# # Based on condition C inherits from A or it inherits from object(not inheritance)

# cond = True

# # inherits from A or B 
# class C(A if cond else object): 
#     def __init__(self, x=None):
#        if cond:
#            super().__init__(x) 
#        else:
#            self.x = x 
#     def isA(self):
#         return isinstance(self, A)



# # Object of C_A 
# ca = C(1) 
# print(ca.isA()) 

