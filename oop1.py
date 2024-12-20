class FirstClass: 
     def setdata(self, value): # Define class methods
         self.data = value # self is the instance of object
     def display(self):
         print(self.data) 
         
         
         
x = FirstClass() 
y = FirstClass() 


print(x)
print(y)
print(isinstance(x, FirstClass))

print("##########################")

x.setdata("Ahmed") # Runs: FirstClass.setdata(x, Ahmed)
y.setdata(3.14159) # Runs: FirstClass.setdata(y, 3.14159)
x.display()
y.display()

print("##########################")

x.data = "New value" # Can get/set attributes
x.display()

print("##########################")

x.anothername = "xspam" # Can set new attributes here too!
y.anothername = "yspam"
print(x.anothername)

