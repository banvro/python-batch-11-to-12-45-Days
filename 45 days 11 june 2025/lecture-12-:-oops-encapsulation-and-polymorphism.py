# # OOPs

# # 8) Encapsulation

# # 9) Polymorphism






# Encapsulation
#     ---> Capsule
#     wrrapperr

#     ----> when we wrap methods, attributes or properties in a single unit is called encapsulation

# class xyz:
#     def mthd1(self):
#         print("this is metod 1")
    
#     def mthd2(self):
#         print("this is method 2")
    
#     def mthd3(self):
#         print("this is method 3")

# ob = xyz()
# ob.mthd2()



# ---> Access Spacifires:
#         Types:
#             1) Public Mambers
#             2) Protected Mambers
#             3) Private Mambers

# 1) Public Mambers
#     ---> are those mambers which are accessable anywhere.

# class xyzz:
#     def __init__(self):
#         self.num1 = 300
#         self.num2 = 400
    
#     def addding(self):
#         print("this is adding..")

#     def subtract(self):
#         print("thhis is subtract")

# xy = xyzz()
# print(xy.num2)



#  2) Protected Mambers
#         --> accessable within the or subclass.
        
# public mambers ---> protected mamber
# (same)

# to make a mamber protect : _

# class xyzz:
#     def __init__(self):
#         self.num1 = 300
#         self._num2 = 400
    
#     def addding(self):
#         print("this is adding..")

#     def subtract(self):
#         print("thhis is subtract")

# class pqr(xyzz):
#     def multi(self):
#         print(self._num2)

# xy = pqr()
# xy.multi()



# 3) Private Mambers:
#     ---> accesable within the class.
    
#     to make mambers private : __


# class xyzz:
#     def __init__(self):
#         self.__num1 = 300
#         self._num2 = 400
    
#     def __addding(self):
#         print("this is adding..")

#     def subtract(self):
#         print("thhis is subtract")

# obj = xyzz()
# print(obj.__num1)

# class pqr(xyzz):
#     def multi(self):
#         print(self.__num1)

# xy = pqr()
# xy.multi()



# class xyzz:
#     def __init__(self):
#         self.__num1 = 300
#         self._num2 = 400
    
#     def __addding(self):
#         print("this is adding..")

#     def subtract(self):
#         self.__addding()
#         print(self.__num1)


# obj = xyzz()
# obj.subtract()




# Polymorphism:
    
#     Ploy : Many
        
#     Morphism : Forms


#     ----> when we have multiple forms of a single things is called polymorphism.
    
#     Types:
#         1) Compile time polymorhusm
#             1) Operator Overloading
#             2) Method Overloading
            
        # 2) Run time polymorphism
        #     1) Method Overriding



#  2) Method Overloading:
#      ---> when we have multiple methods with the same name. 
#         so when call that method. then which one method is call is completly depends on number of arguments we pass at calling time.

# ----> python doent support method overloading

# class xyzz:
#     def summ(self, a, b, c):
#         zx = a + b + c
#         print(zx)
    
#     def summ(self, a, b):
#         zx = a + b
#         print(zx)
        
#     def summ(self, a):
#         zx = a 
#         print(zx)

# obj = xyzz()
# obj.summ(23, 34)


# a = 10

# a = 20

# print(a)

# -------------------------------------

# 1) Operator Overloading

# 200 + 400

# operends : 200, 400

# operator : +

# 10 + 20

# +  ---> function(),  __add__
# - -----> __sub__
# * -----> __multi__
# % ----> __mod__


# print(20 + 10)

# class xyzz:
#     def __init__(self, x, y):
#         self.num1 = x
#         self.num2 = y
        
#     def summ(self):
#         print("heloooooooooo")
    
#     def __add__(ab, ac):
#         zx = ab.num1 + ac.num1
#         c = ab.num2 + ac.num2
#         return zx, c
    
# obj =  xyzz(23, 10)

# obj1 = xyzz(30, 12)

# z = obj + obj1
# print(z)
    
    
    
    
# x = 10

# x = 1000

# print(x)
    
    
  1) Method Overriding:
        when we craete an object in parent class and also we create method in child class with same name. then we create obect of child class or call that method,  then the chlid class method is executed.

class abcc:
    def a(self):
        print("this is aaaa")
    
    def b(self):
        print("this is bbbbb")

class xyzz(abcc):
    def a(self):
        print("zzzzzzzz")

obj = xyzz()
obj.a()






--------------------------

Excpetion Handeling  +  regex

Projects



