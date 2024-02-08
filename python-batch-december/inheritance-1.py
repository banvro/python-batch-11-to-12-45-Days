# OOPs :
#     1) class
#     2) object
#     3) self
#     4) constructor
#     5) Methods
#     6) Attributes
    
#     7) Inheritance : 
#         1) Single Level Inheritance
#         2) Multilevel Inheritance
#         3) Multiple Inheritance
#         4) Hirerichical Inheritance
#         5) Hybrid Inheritance

# class mycls1:
#     def mthd1(self):
#         print("I am method 1")
    
#     def mthd2(self):
#         print("i am method 2")
    
#     def mthd3(self):
#         print("i am method 3")
# obj = mycls1()  
# obj.mthd2()

# class mycls2(mycls1):
#     def mthd4(self):
#         print("i am method 4")

# xyz = mycls2()
# xyz.mthd4()
# xyz.mthd1()

# obj = mycls1()
# obj.mthd4()



# single level inheritance :
#     1 parent have 1 child



# 2) multiple inheritance:
    # 1 child have multiple parent

# class cls1:
#     def mthd1(Self):
#         print("this is method 1")

#     def mthd2(self):
#         print("this is method 2")
    
# class cls2:
#     def mthd3(self):
#         print("this i method 3")

# class cls3(cls1, cls2):
#     def mthd4(self):
#         print("this is method 4")

# obj = cls3()
# obj.mthd1()



# 3) MultiLevel Inheritance:
#     grantparent <- parent <- child
    
# class cls1:
#     def mthd1(self):
#         print("this is method 1")
    
#     def mthd2(self):
#         print("this is method 2")

# class cls2(cls1):
#     def mthd3(self):
#         print("this is method 3")

# class cls3(cls2):
#     def mthd4(self):
#         print("this is method 4")

# obj = cls3()
# obj.mthd1()





# class mycls1:
#     def _init_(self):
#         self.num1 = 10
#         self.num2 = 200

#     def car(self):
#         print("this is a car")


# obj = mycls1()
# obj.car()

# print(obj.num2)
# class mycls2(mycls1):
#     pass

# obj = mycls2()

# # obj.car()
# print(obj.num2)






# panding do this tommrow 
# class savedata:
#     def _init_(self, a, b, c):
