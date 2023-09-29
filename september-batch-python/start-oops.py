# 1) OOps
# 2) Class
# 3) object
# 4) sellf
# 5) constructer
# 6) attributes
# 7) methods

# 8) inharitance
#     1) sigle inharitance
#     2) mutlipal inahritance
#     3) multilevle inharitance
#     4) hirarical inahritance
#     5) hibrid inharitance

# 9) abstraction
#     1) abstract classes
#     2) interfaces
#     3) abstract method

# 10) Encapsulation
#     Access Sapcifires
#         public mambers
#         private mambers
#         protected mambers

# 11) Polymorphiusm
#     1) duck typing
#     2) method overloading
#     3) method overrriding
#     4) oprator overloading

# OOps : class or objects

# from functools import reduce


# classs : is a blueprint of an object 

# object : instance of a class 

# self : for refrencing 

# class xyz:
#     def car(self, a, b):
#         c = a + b
#         print(c)
    
#     def bus(self):
#         print("i am a bus..")
        
# obj = xyz()
# obj.car(10, 20)




# Constructer __init__, is call automaticlly while object is created

# class cls1:
#     def __init__(self):
#         print("heloo i am constructer..")
    
#     def car(self):
#         print("i am car..")
        
# obj = cls1()
# obj.car()


# class xyz:
#     def car(self, a, b):
#         c = a + b
#         print(c)
    
#     def bus(self):
#         print("i am a bus..", a)
        
# obj = xyz()
# obj.car(10, 20)

# obj.bus()


# Attrebutes: 


# class cls1:
#     def __init__(self, a, b):
#         self.first_name = a
#         self.last_name = b
    
#     def car(self):
#         print("i am a car..", self.first_name, self.last_name)

# xyz = cls1("kriss", "moris")

# xyz.car()


class calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def sum(self):
        print(self.num1 + self.num2)
    
    def multi(self):
        print(self.num1 * self.num2)
    
    def sub(self):
        print(self.num1 - self.num2)

obj = calculator(20, 10)        
obj.multi()



# oops
# class
# object
# consrcuer
# self
# attrebutes
# methoda






















    
    
    
    
    
    