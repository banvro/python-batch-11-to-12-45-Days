# class 
# object
# self
# constructer
# methids
# attrebutes

# 1) Inharitance : 
#     1) single inharitance
#     2) multipal inhariatnce
#     3) multilevel inharitance
# #     4) hirarical inharitance
# #     5) hibrid inharitance

# 1) single inharitence :

# class cls1:
#     def mthd1(self):
#         print("i am from class 1 a dmthd 1")
    
#     def mthd2(self):
#         print(" i am from class 1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mthd3")
        
        
# obj = cls2()
# obj.mthd1()




# 2) multipal inharitance: 
    
# class cls1:
#     def mthd1(self):
#         print("i am from class 1 a dmthd 1")
    
#     def mthd2(self):
#         print(" i am from class 1 and mthd 2")
        
# class cls2:
#     def mthd3(self):
#         print("i am from class 2 and mthd3")
        
# class cls3(cls1, cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd2()


# 3) multilevel inahritance:

# class cls1:
#     def mthd1(self):
#         print("i am from class 1 a dmthd 1")
    
#     def mthd2(self):
#         print(" i am from class 1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mthd3")
        
# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()




# 4) hiraricl inharitnce 

# class cls1:
#     def mthd1(self):
#         print("i am from class 1 a dmthd 1")
    
#     def mthd2(self):
#         print(" i am from class 1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mthd3")
        
# class cls3(cls1):
#     def mthd4(self):
#         print("i am from class 3")
        
# obj = cls3()
# obj.mthd1()



# 5) hibrid inharitance 


# class cls1:
#     def mthd1(self):
#         print("i am from class 1 a dmthd 1")
    
#     def mthd2(self):
#         print(" i am from class 1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mthd3")
        
# class cls3(cls2):
#     def mthd4(self):
#         print("i am from class 3")

# class cls4(cls2, cls3):
#     def mthd5(self):
#         print("i am from class 4")
        
# obj = cls3()
# obj.mthd1()




# 1) single inharitance :  1 parent or 1 child

# 2) multipal inahritance : when i child have multipal parensts

# 3) multilevel inahritance : when a bottem class inharited from their upper class

# 4) hirarical inahritance : 1 parent have multipal child

# 5) hibrid inharince : combintion of more then 1 classes








# Encapsulation : 

# when multipal things bind in a single unit


# class cls1:
#     def mthd1(self):
#         print("this is first methid")
    
#     def mthd2(self):
#         print("this is seond method..")

# obj = cls1()


# Access Spacifires :
    # 1) public
    # 2) privte  __
    # 3) protected _


# class cls1:
#     def __init__(self):
#         self.num1 = 10
#         self.__num2 = 2000
        
#     def __mthd1(self):
#         print(self.num1 + self.__num2)
    
#     def mthd2(self):
#         print("this is seond method..")

# obj = cls1()
# obj.__mthd1()

# print(obj.__num2)

