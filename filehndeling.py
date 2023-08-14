# OOps:
    # 1) Inharitance
    # 2) Abstraction
    # 3) ENcapsulation
    # 4) Polymrphisum
    
# objects
# claases
# self
# constructer
# super()


# Abstraction : data hinding  

# from abc import ABC, abstractmethod
# # abc => abstract base class

# # interface
# class clas1(ABC):
#     @abstractmethod
#     def car(self):
#         print("This is a car")
    
#     def bus(self):
#         pass
    
#     @abstractmethod
#     def plane(self):
#         pass

# class clas2(clas1):
#     def mthd1(self):
#         print("i am ok")
    
#     def car(self):
#         print("ok")
    
#     def plane(self):
#         print("Done")

# obj = clas2()
# obj.car()


# from abc import ABC, abstractmethod

# class fields(ABC):
#     @abstractmethod
#     def name(self):
#         pass
    
#     @abstractmethod
#     def age(self):
#         pass
    
#     @abstractmethod
#     def phonenumber(self):
#         pass

# class filldata(fields):
#     def done(self):
#         print("no")
    
#     def name(self):
#         print("this is name")

#     def age(self):
#         print("this is age")
    
#     def phonenumber(self):
#         print("this is phonenumber")
    

# obj = filldata()





# Encapsulation : binding up data in a single unit..

# class xyz:
#     def abc(self):
#         print("nooo")
    
#     def car(self):
#         print("done....")

# Access Spacifires
# 1) Public mambers
# 2) Protected mambers    _
# 3) Private mambers    __


# class xyz:
#     def __init__(self, a, b):
#         self._num1 = a
#         self.__num2 = b
    
#     def some(self):
#         print(self.__num2)

# class abcs(xyz):
#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)
        
#     def mthd(self):
#         print(self._num1)
    
# obj = xyz(12, 10)
# obj.some()

# obj1 = abcs(12, 10)
# obj1.mthd()






