# OOps:
#     1) inharitance
#     2) ABstraction
#     3) Encapsulation
#     4) Polymorphism


# 4)  Polymorphism

    # poly    :   many
    # morphism    :    forms

    # a) Duck Typing
    # b) Operater Overloading
    # c) Method Overloading
    # d) Method overriding

# a) Duck typing:

# class clas1:
#     def move(self):
#         print(" i am from clas 1")
    
# class clas2:
#     def move(self):
#         print(" i am from clas 2")

# obj1 = clas1()
# obj2 = clas2()


# def duck(a):
#     a.move()

# duck(obj2)



# b) Operater Overloading

# 12 + 10

# class clas1:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def sumthis(self):
#         print(self.num1 + self.num2)
    
#     def __add__(xyz, other):
#         m1 = xyz.num1 + other.num1
#         m2 = xyz.num2 + other.num2
#         sum = clas1(m1, m2)
#         return sum
    

# obj1 = clas1(12, 10)

# obj2 = clas1(20, 30)

# summ = obj1 + obj2


# print(summ.num2)
# # print("10" + "20")


# a = 20


# a = 100

# print(a)



# c) Method Overloading : 

class clas1:
    def sumthis(self, a, b, c):
        z = a + b + c
        print(z)
    
    def sumthis(self, a, b):
        z = a + b
        print(z)
    
    def sumthis(self, a):
        z = a
        print(z)

obj = clas1()

obj.sumthis()



# class clas1:
#     def sumthis(self, a, b, c):
#         z = a + b + c
#         print(z)
    
#     def sumthis(self, a, b):
#         z = a + b
#         print(z)
    
#     def sumthis(self, a):
#         z = a
#         print(z)

# obj = clas1()

# obj.sumthis(12)


# def xyz(a = 12, b = 20):
#     c = a + b
#     print(c)

# xyz(b = 100)





# default perameter
# class clas1:
#     def sumthis(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             z = a + b + c
#             print(z)
        
#         elif a != None and b != None:
#             z = a + b
#             print(z)
        
#         elif a != None:
#             z = a
#             print(z)
            
# obj = clas1()
# obj.sumthis(10, 100, 10)
        




# Method overriding:


# class clas1:
#     def car(self):
#         print(" i am car")
    
#     def bus(self):
#         print(" i am bus")
        
# class clas2(clas1):
#     def train(self):
#         print("i am tran")
    
#     def car(self):
#         print("no i am not a car")

# obj = clas2()

# obj.car()









