#An abstract method is a function blueprint with no implementation
# (just a declaration) thatmust be defined in child classes



from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 


class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 



R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 
