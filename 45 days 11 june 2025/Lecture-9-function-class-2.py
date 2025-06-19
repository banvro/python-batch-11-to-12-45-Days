# Functions:
#     function
#     arguments perameters
#     Types
    
# lambda function 

# anonymous function in python

# ----> small functionaly

# def 

# lambda ---> single line function

# Syntax:
    
# lambda permeters : expression


# def addd(a, b):
#     zx = a + b
#     print(zx)

# addd(100, 232)


# x = lambda a, b : print(a + b)


# x(12, 3)

# x(1, 2)


# squre(2)



# sqr = lambda x : print(x ** 2)

# sqr(5)


# use caes:

# map()
# filter()
# reduce()



# map()
#     ---> ittrable object
#     ---> elements ---> operation on each element


# zx = [1, 2, 3, 2, 23, 3, 4]

# lt = []


# for i in zx:
#     zxx = i + 10
#     lt.append(zxx)

# print(lt)


# map():
    

# synatax:
    
# map(lambda_function , ittaable_obj_name)

# lambda peramter : expression

# pqr = [12, 34, 3, 45, 56, 67, 8, 9, 10]

# sqr_dta = map(lambda x : x ** 2, pqr)


# print(list(sqr_dta))



# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ["2 x 1 = 2", "2 x 2 = 4", ........]



# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tbl = map(lambda i : f"2 x {i} = {2*i}", x)

# print(list(tbl))





# filter()

# filtering data

# syntax:

# filter(lambda_function, ittrable_objt)


# zx = [12, 34, 45, 5, 65, 67, 78, 894, 3, 23, 12, 23, 34, 4, 56, 6, 12, 34, 4, 56]


# x = filter(lambda y : y % 2 == 0, zx)


# print(tuple(x))




# zx = [12, 34, 45, 5, 65, 67, 78, 894, 3, 23, 12, 23, 34, 4, 56, 6, 12, 34, 4, 56]

# yz = filter(lambda x : x > 50, zx)


# print(list(yz))



x = [1, 2, 3, 4, 5, 6]


# ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"]


# q = map(lambda y : y * "a", x)


# print(list(q))


# x = [1, 2, 3, 4, 5, 6]

# ["aaaaa", "aaaaa", "aaaa", "aaa", "aa", "a"]

# x = [1, 2, 3, 4, 5, 6]


# yq = map(lambda y : (7-y) * "a", x)

# print(list(yq))




# aq = ["this", "hey", "car", "no", "heyu", "good", "python", "donee", "okkkkk"]

# # len --->4 , more then 4


# x = filter(lambda x : len(x) >= 4, aq)


# print(tuple(x))


# -----------------------------------

# Partial function:
#     if we have existing function or we want to create a new function by using that exisiting function, by setting up the default value some of the exsitng functioin's perameters
    

# def power(a, b):
#     zx = a ** b
#     print(zx)

# power(3, 3)


# def sqr(x):
#     zx = x ** 2
#     print(zx)

# sqr(5)


# def power(a, b):
#     zx = a ** b
#     print(zx)

# power(3, 3)

# from functools import partial

# # syntax

# # partial(exisitng_fun, perameter1, perameter2)

# sqr = partial(power, b = 2)

# sqr(100)




# addthree(12, 34, 45)


# partial_function

# addtwo


# def addthree(x, y, z):
#     zx = x + y + z
#     print(zx)

# addthree(10, 20, 30)

# from functools import partial

# addtwo = partial(addthree, z = 0)

# addtwo(10, 30)


# Dacorators:











# reduce() :

# reduce(lambda_function, ittable obj)

# from functools import reduce

# zx = [1, 2, 3, 2, 3, 2, 3, 4, 2, 3]


# e = reduce(lambda x, y : x + y, zx)

# print(e)



# Dacorator
#     -----> dacorate functions
#     ---> to inhance the functionality of an function



# creating a dacorator

# def daco(x):
#     def waper():
#         print("wecome to my function...")
#         print("designed by Gudo\n")
#         x()
#         print("\n")
#         print("thank you for usiing me")
        
#     return waper

# @daco
# def xyz():
#     print("helo.....")

# # xyz()


# @daco
# def hlo():
#     x = input("Enter first numer : ")
#     y = input("ENter seodn number : ")
    
#     z = int(x) + int(y)
#     print(z)
    
# hlo()





def daco(x):
    def waper(*args, **kwargs):
        print("wecome to my function...")
        print("designed by Gudo\n")
        x(*args, **kwargs)
        print("\n")
        print("thank you for usiing me")
        
    return waper

@daco
def summ(a, b):
    zx = a + b
    print(zx)

summ(12, 20)

@daco
def xyz(a, b, x):
    zx = a + b + x
    print(zx)

xyz(10, 20, 30)



# -----------functions done------------

