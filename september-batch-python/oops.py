# # # OOPs : 
# # qw = [2, 3, 12, 90, 67, 1, 200, 45]

# # minn = qw[0]  # 2, 1
# # maxx = qw[0]  # 2, 3, 12

# # for i in qw:
# #     # 2 > 1
# #     if minn > i:  
# #         minn = i
        
# #         2 < 12
# #     elif maxx < i:
# #         maxx = i
    
# # print(minn)
# # print(maxx)

# # OOps = object oriented programmin

# # class
# # objects


# 1) class
# 2) object
# 3) self
# 4) constructer
# 5) methods
# 6) abttributes
# 7) Inharitance
#     1) single inharitance
#     2) multipal inharitance
#     3) multilevel inhritance
#     4) hirarical inharitance
#     5) hibrid inharitance

# 8) abstraction
#     abstract class
#     interfaces
#     abstract methods

# 9) Encapsulation
#     access spacifires
#         1) public mambers
#         2) private mambers
#         3) protected mambers

# 10) Polymorphisum:
#     1) Duck Typing
#     2) mehtod overloading
#     3) mehtod overriding
#     4) operator overloading
    



# Class : class is bluprint of an object

# objects : instance of a class

# self = use for ranfrenceing 

# class xyz:
#     def car(self):
#         print("i am a car")
    
#     def bus(self):
#         print("i am a bus")

# obj = xyz()
# obj.bus()

# obj1 = xyz()






# cunstucter : __init__(), it class automatically while we create an objects



# constructer is useed to initlize attrebutes

# class sumthis:
#     def __init__(self):
#         print("heloo i am cnstructer..")
    
#     def xyz(self, a, b):
#         c = a + b
#         print("the sum is : ", c)

#     def bus(self):
#         print("i am bus", a)

# obj = sumthis()
# obj.xyz(12, 10)

# obj.bus()


# class mycls:
#     def __init__(self, a, b):
#         self.name = a
#         self.age = b
    
#     def sumthis(self):
#         print("i am sum", self.name)

#     def car(self):
#         print(f"{self.name} have {self.age} age")

# obj = mycls("kriss", 20)
# ob1 = mycls("ayush", 21)

# ob1.car()


# Inharitance : to get some properties from anther class we use inharitance


# # 1) single inharitance

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")
        
# obj = cls2()
# obj.mthd1()



# obj = cls1()
# obj1 = cls2()
# obj1.mthd3()






# # multipal inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2:
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls1, cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd3()





# # multilevel inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()





# # hirical inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls1):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()







# hybrid inharitance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1")

#     def mthd2(self):
#         print("i am from class 1 and mthfd 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2")

# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")

# class cls4(cls2, cls3):
#     def mthd5(self):
#         print("i am from class 4")
        
# obj = cls3()
# obj.mthd1()



# 2) abstraction : data hiding

# abstract classes
# abstract method
# interfaces

# abc = abstract base class

# from abc import ABC, abstractmethod

# class cls1(ABC):
#     @abstractmethod
#     def car(self):
#         pass
    
#     @abstractmethod
#     def train(self):
#         print("i am train")

# class cls2(cls1):
#     def bus(self):
#         print("i am bus")
    
#     def car(self):
#         print("i am car")
    
#     def train(self):
#         print("i am train")
        
# obj = cls2()
# obj.car()









# 3) Encapsulation : to bind up multipal things in a single unit


# Access Spacifiers
# 1) Public Mambers
# 2) Private Mambers __
# 3) protected mambers _

# class cls1:
#     def __init__(self):
#         self.__a = 10
#         self.b = 20
    
#     def sumthis(self):
#         print(self.__a + self.b)
    
# class cls2(cls1):
#     def hlo(self):
#         print(self._cls1__a)
        
# obj = cls2()
# obj.hlo()

# obj = cls1()
# print(obj.b)



# Polymorphiusm  :

# poly  : many

# morphiusm  : forms

# types of polymorphium : 
# 1) compile time polymorphisum
    # 2) method overloading
    # 3) operator overloading

# 2) run time polymorphiusm
    # 5) method overriding


# 1) Duck typing
# 2) method overloading
# 3) operator overloading
# 5) method overriding

# class cls1:
#     def helo(self):
#         print("i am for class 1")

# class cls2:
#     def helo(self):
#         print("i am form class 2")

# obj1 = cls1()
# obj2 = cls2()

# def show(x):
#     x.helo()

# show(obj2)


# 1) operator overloading

# a = 10

# a = 100

# print(a)


# a + b


# 10 + 20

# operator = +
# operands = 10, 20


# a = 10
# b = 20

# c = a + b







# a = 10
# b = "12"

# print(a + b)


# class cls1:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def sumx(self):
#         print("askjdb")
    
#     def __add__(first, second):
#         qw = first.a + second.a
#         wq = first.b + second.b
#         sum = cls1(qw, wq)
#         return sum
        
# obj1 = cls1(10, 30)
# obj2 = cls1(30, 90)

# xc = obj1 + obj2
# print(xc.b)

# a = 10
# a = 100



# 3) method overloading:

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
# obj.sumthis(10)


# class xyz:
#     def sumthis(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             zx = a + b + c
#             print(zx)
        
#         elif a != None and b != None:
#             zx = a + b
#             print(zx)
        
#         elif a != None:
#             zx = a
#             print(zx)

# obj = xyz()
# obj.sumthis(12)


# 4) method overriding:

# a = 10
# a = 100

# class xyz:
#     def mthd1(self):
#         print("i am a mthod1 ")
    
#     def mthd2(self):
#         print("iam mrhod 2")

# class pqr(xyz):
#     def mthd1(self):
#         print("i ma ffrom clsss pqr")

# obj = pqr()
# obj.mthd1()











# Functions 

# lambda 
# map()
# filter()
# reduce()


# lambda function 

# def sumthis(a, b):
#     c = a + b
#     print(c)
    
# sumthis(12, 20)


# lambda arguments : expression

# zx = lambda a, b : a + b

# print(zx(12, 10))


# sq = lambda a : a + 20000

# print(sq(10))



# map() : 


# lst = [2, 6, 7, 10, 9, 78, 100]

# # map(function itrater )

# zx = map(lambda i : i + 10, lst)

# print(list(zx))



# filter(function, itrater,)

# zx = [12, 10, 9, 67, 56, 30, 31, 91]

# zx = filter(lambda a : a % 2 != 0, zx)
# print(list(zx))

# reduce

# from functools import reduce

# ae = [12, 10, 20, 1, 2, 3]


# zx = reduce(lambda a, b : a + b, ae)

# print(zx)

# b = 0
# for i in a:
#     b = b + i

# print(b)



# comperhension :

# []
# ()

# zx = [i for i in range(1, 10) if i % 2 == 0]

# print(zx)



# [expression loop condation]

zx = int(input("ENter number of inputes your wish to enter : "))

inp = [int(input(f"Enter #{i + 1} number : "))for i in range(zx) ]


# print(inp)

# print(sum(inp))
# q = 0
# for i in inp:
#     q = q + i
    

# print(q)

def xyz(*a):
    print(a)

xyz(*inp)


























































































































