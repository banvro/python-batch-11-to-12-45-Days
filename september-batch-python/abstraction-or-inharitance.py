# Inharitance
# Encapsulation
# Polymorphiusm
# Abstraction



# Abstraction : use for data hiding 

# 1) abstract class
# 2) interfaces
# 3) abstract methods

# abc = abstract base class 

# from abc import ABC, abstractmethod

# class cls1(ABC):
#     @abstractmethod
#     def name(self):
#         pass
        
#     @abstractmethod
#     def age(self):
#         pass

# class cls2(cls1):
#     def hlo(self):
#         print("i am hello")
    
#     def name(self):
#         print("i am a new name")
    
#     def age(self):
#         print("this is new age..")

# obj = cls2()
# obj.hlo()






# 4) Polymorphisum :
    # 1) compile time polymorphiusm
    #     1) method overloading
    #     2) operator overloading
    
    # 2) run time polymorphisum
    #     1) method overring
    
    
    
# 1) method overloading  

# class cls1:
#     def sumthis(self, a, b, c):
#         zx = a + b + c
#         print(zx)
    
#     def sumthis(self, a, b):
#         zx = a + b
#         print(zx)
    
#     def sumthis(self, a):
#         zx = a 
#         print(zx)

# obj = cls1()
# obj.sumthis(12, 23)




# a = 10
# a = 20

# class cls1:
#     def shumthis(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             zx = a + b + c
#             print(zx)
#         elif a != None and b != None:
#             zx = a + b
#             print(zx)
#         elif a != None:
#             zx = a
#             print(zx)
# obj = cls1()
# obj.shumthis(12)




# class cls1:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def hlo(self):
#         print("this is helow")
    
#     def __add__(x, y):
#         qw = x.num1 + y.num1
#         er = x.num2 + y.num2
#         sum = cls1(qw, er)
#         return sum

# obj1 = cls1(10, 20)
# obj2 = cls1(20, 100)

# zx = obj1 + obj2
# # 10 + 20
# print(zx.num2)



# 3) methd overdding

class cls1:
    def car(self):
        print("i am car")
    
    def bus(self):
        print("this is busss")

class cls2(cls1):
    def hlo(self):
        print("i am hlo")
    
    def car(self):
        print("noooooo")

obj = cls2()
obj.car()










