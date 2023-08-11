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

# class mydata:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def summ(self):
#         print(self.num1 + self.num2)

# obj = mydata(12, 10)
# obj.summ()



# obj1 = mydata(100, 200)
# obj1.summ()


# class
# object
# self
# constructer


# Inhritance : to get some properties from their parent class

# 1) Parent class
# 2) Child class (Subclass)

# class clas1:
#     def mthd1(self):
#         print("I am from class 1 and mthd 1")
    
#     def mthd2(self):
#         print("I am from class 1 and mthd 2")

# class clas2(clas1):
#     def mthd3(self):
#         print("I am from class 2 and mthd 3")

# obj = clas2()

# obj.mthd2()



class cls1:
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def storedata(self):
        print(f"{self.name} have the {self.age}  age")
    
    
# obj = cls1("Kriss", 20)
# obj.storedata()
    
    
class cls2(cls1):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.phone_number = c
        
    def sum(self):
        print(f"{self.name} have the {self.age}  age and his phone number is {self.phone_number}")

obbj = cls2("Moris", 20, "9287346432")

obbj.sum()





