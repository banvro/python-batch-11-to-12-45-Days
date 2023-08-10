# OOps (Object Oriented Programming) : 
#     1) Inharitance
#     2) Abstraction
#     3) Encapsulation
#     4) Polymorphisum

# oops => Class or objects

# class => is a blueprint of an object.

# object => is an instance of the class


# class clas1:
#     def car(self):
#         print("I am car")
    
#     def bus(self):
#         print("I am bus")
    
#     def paln(self):
#         print("i am a plane")
        
# obj = clas1()

# obj.car()


# constructer

# class myclass:
#     def __init__(self):
#         print("I am constucter")
        
#     def paln(self):
#         print("i am a plane")


# obj = myclass()

# obj1 = myclass()

class mydata:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def summ(self):
        print(self.num1 + self.num2)

obj = mydata(12, 10)
obj.summ()


obj1 = mydata(100, 200)
obj1.summ()





