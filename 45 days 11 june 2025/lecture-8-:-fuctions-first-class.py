# Python
# condational statments 
# Loops
# Data Structer:
#     1) list
#     2) tuple
#     3) set
#     4) Dictionry
  
# functions  ---> 3
# oops ------> 4 - 5
# exception handling  ---> 1
# Database -----> SQL ----> 3--4

# tkinter ----> projects



# functions:
#     ---> block of code
#         --> repete
        
# print("hellow wplrd")
# print("ok")
# ksjbfsdf
# sdfjsbdkfjsbfks
# print("hellow wplrd")
# print("ok")
# sdfsdfsdjfbsk
# print("hellow wplrd")
# print("ok")


# -------> code optimization
#     ---> length reduce




# synatx

# def function_name():
#     # code.......


# core function

#  type of  functions:
#      1) built in functions
#             1) print()
#             2) input()
#             3) count()
#             4) len()
            
#      2) user define function


# declearation of function

# def xyz():
#     print("hellow world")
#     print("heoww are youuuu")


# # calling a function

# xyz()

# xyz()

# xyz()

# xyz()


# a = 10
# b = 20
# c = a + b
# print(c)



# x = 1
# y = 2
# z = x + y
# print(z)


# def summ():
#     x = 1
#     y = 2
#     z = x + y
#     print(z)


# summ()

# summ()



# Perameters and arguments

# Perameters:
#     are the veriables we pass in () at declration time

# def xyz(a):
#     print("hellow", a)


# # argument
# xyz("Kriss")


# xyz("Python")


# def summ(x, y):
#     zx = x + y
#     print(zx)


# summ(12, 10)

# summ(1, 2)
# summ(1000, 3434)


# problem:
    
# table(35)


# 2 x 1 = 2
# 2 x 2 = 4
# .
# .


# def table(q):
#     for i in range(1, 11):
#         print(f"{q} x {i} = {q*i}")


# table(4)


# function
# peramters
# arguments


# def xyzz(a, b):
#     zx = a + b
#     print(f"the sum of {a} and {b} is  : {zx}")

# xyzz(12, 45)


# xyzz(3, 7)



# Types of arguments and perameters:
#     1) Postational perameters
#     2) keyword arguments
#     3) Default arguments
#     4) veriable length peramerts:
#         1) *args
#         2) **kwargs


# 1) Postational perameters:

# def infoo(name, age):
#     print(f"user name is {name} and age is {age}.")

# infoo("Python", 24)


# 2) Keyword arguments:

# def infoo(name, age):
#     print(f"user name is {name} and age is {age}.")

# infoo(age = 24, name = "Python")



# function:

# factorial(5)

# 5 x 4 x 3 x 2 x 1 = 120

# factorial(3)

# 3 x 2 x 1 = 6


# def factorial(q):
#     ml = 1
#     st = ""
    
#     for i in range(q, 0, -1):
#         st = st + str(i) + " x "
#         ml = ml * i
        
#     st = st[: -2]

#     print(st, "=", ml)

# factorial(10)



# def factionrial(r):
#     st = ""
#     mlt = 1
    
#     for i in range(r, 0, -1):
        
#         st = st + str(i) + " x "
#         mlt = mlt * i
        
#     st = st[: -2]
#     print(st, "=", mlt)

# factionrial(5)






#  3) Default perameters
#     ---> when we do not know, user pass value or not


# def summ(a = 0, b = 0, c = 0):
#     zx = a + b + c
#     print(zx)

# summ()


#  4) veriable length peramerts:
#         1) *args
#         2) **kwargs


# ---> when we do not know, how many arguments user pass.



# 1) *args ---> arbitrary postatinal arguments


# def summ(*args):
#     print(args)


# summ(12, 23, 34, 45, 6, 7, 89)



# def summ(*x):
    
#     sm = 0
    
#     for i in x:
#         sm = sm + i
#     print(sm)


# summ(2, 4, 5, 6)




# 2) **kwargs :
#     --> dictionry

def info(**x):
    print(x)

info(name = "kriss", age = 20)

