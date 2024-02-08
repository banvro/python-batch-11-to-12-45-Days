class
object
self
constructor
methods
attributes


# class calculator:
#     def sumthis(self, a, b):
#         z = a + b
#         print("the sum is :", z)
    
#     def substraction(self, a, b):
#         z = a - b
#         print(z)

# xyz = calculator()
# xyz.sumthis(12, 10)

# xyz.substraction(100, 23)



# constructoe : this is spacial method in a class design by uing _init_. the main funcationlity of constructor is, it calls automatically for while an object is created of an class. it is used to initilizae attribues.

class mycls:
    def _init_(self, x, y):
        print("i am cnstructor and i am call automatically..")
        
    def car(self):
        print("i am simple method")

obj = mycls()


# constructoe : this is spacial method in a class design by uing _init_. the main funcationlity of constructor is, it calls automatically for while an object is created of an class. it is used to initilizae attribues.


# attributes:
    
    
class calculator:
    def _init_(self, x, y):
        self.num1 = x
        self.num2 = y
    
    def sumthis(self):
        print(self.num1 + self.num2)
    
    def substraction(self):
        print(self.num1 - self.num2)
    
    def multi(self):
        print(self.num1 * self.num2)
    
    def devsion(self):
        print(self.num1 / self.num2)

mycal = calculator(12, 5)
mycal.sumthis()
mycal.substraction()
