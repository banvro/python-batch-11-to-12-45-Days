# 1) Function:
# 2) types of function
#     1) built in 
#     2) user define function

# 3) Perameters, arguments
# 4) types of Peramters
#     1) Postional Perameters
#     2) Keyword arguments
#     3) Default Peramters
#     4) Veriable length peramters
#         1) *args
#         2) **kwargs

# 5) Lambda function
# 6) map(), filter(), reduce()

# 7) Decorator

# 8) Recursion : when a function calling itself and fall in a infinite loop is called recursion


# def showdata():
#     print("hwlloooo")
#     showdata()


# showdata()

# factorial:
#     5 = 5 x 4 x 3 x 2 x 1 = 120


            #   5, 4
# def factorial(a):
#     if a < 1 or a < 0:
#         return 1
#     return a * factorial(a - 1)
        #   5 * factorial(4)
        #       4 * factorial(3)
        #           3 * factorial(2)
        #               2 * factorial(1)
                        #   1 * factorial(0)
                        #       0 * factorial(-1)
    
# zx = factorial(4)
# print(zx)



# 9) Partial Function : 



# def car():
#     a = 10
#     return a
    
# zx = car()
# print(zx)

# print(a)

# def sumthis(a, b):
#     zx  = a + b
#     return zx

# t = sumthis(10, 30)

# zxr = t + 100

# print(zxr)



# 10) Partial function : 


# def power(a, b):
#     zx = a ** b
#     print(zx)

# power(2, 10)

# def sequer(s):
#     zx = s ** 2 
#     print(zx)

# sequer(3)

from functools import partial

def power(a, b):
    zx = a ** b
    print(zx)

# power(2, 10)

# seq = partial(oldfun, assignvalues)

seq = partial(power, b = 2)

seq(20)


partial function is help to carete a new function by using existing function. in this we fix some argumnets.
