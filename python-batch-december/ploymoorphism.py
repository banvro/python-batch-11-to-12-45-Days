# Polymorphisum:
#     poly : Many
#     morphism : forms

# 1) Compile Time Polymorism
#     1) Method Overloading
#     2) Operator Overloading
    
# 2) Run Time Polymorphism
#     1) Method Overriding



# Operator Overloading: 
    
# 10 + 20


# operands = 10, 20
# operator = +
    
    
# print(True + True)

# class mycls:
#     def _init_(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def xyz(self):
#         print("this is xyz method")
    
#     def _add_(self, another):
#         zx = self.num1 + another.num1
#         xy = self.num2 + another.num2
#         sum = mycls(zx, xy)
#         return sum
        

# obj = mycls(10, 30)

# obj1 = mycls(23, 78)

# c = obj + obj1

# print(c.num2)


# 1) Method Overriding

# a = 10

# a = 90

# print(a)
    

# class cls1:
#     def car(self):
#         print("this is car")
    
#     def bus(self):
#         rint("this is bus")

# class cls2(cls1):
#     def train(self):
#         print("this is tain")
    
#     def car(self):
#         print("carrrrrrrrrr")
    
# obj = cls2()
# obj.car()  
    

# 1) Method Overloading

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
# obj.sumthis(12, 34)

# a = 10
# a = 100


# class cls1:
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

# obj = cls1()
# obj.sumthis(12, 34, 45)


zx = 6

for i in range(1, zx + 1):
    print(" " * (zx - i) + "* " * i)

# for i in range(zx - 1, 0, -1):
#     print(" " * (zx - i) + "*  " * i)
