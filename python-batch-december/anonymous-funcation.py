# anonymous function in python:

# Function: 
# peramters
# arguments

# anonymous function in python:


# def sumthis(a, b):
#     c = a + b
#     print(c)
    
# sumthis(12, 10)


# lambda functions

# # lambda arguments : expression

# zx = lambda a, b : print(a + b)

# zx(100, 200)


# seq = lambda a : a ** 2

# print(seq(10))


# 1) map()
# 2) filter()
# 3) reduce()

# # lambda arguments : expression

# 1) map() : 
    
# lst = [2, 1, 3, 2, 3, 2, 3, 1, 6, 5, 3, 10]

# map(lambda function, itrator)

# zx = map(lambda x : x + 10, lst)

# print(list(zx))


# a = "abcdefg"

# zx = map(lambda a : a + str("ooooo"), a)

# print(tuple(zx))




# 2) filter : 


# lst = [2, 32, 7, 4, 6, 1, 3, 9, 4, 6, 3, 6, 10]

# # filter(lambda, itrator)

# zx = filter(lambda a : a % 2 == 0, lst)

# print(list(zx))




# zx = ["a", 1, "b", 120, "car"]

# xyz = filter(lambda a : type(a) == int, zx)


# print(tuple(xyz))


# 3) reduce() : 

# lst = [12, 20, 56, 4, 12, 10]


# x = 0

# for i in lst:
#     x = x + i

# print(x)

# from functools import reduce

# lst = [12, 20, 56, 4, 12, 10]


# zx = reduce(lambda a, b : a + b, lst)

# print(zx)





# Decorator : 

# def my_dacorator(myfun):
#     def wrappper():
#         print("welcom to my function..")
        
#         myfun()
        
#         print("thank you for using my function :)")

#     return wrappper


# @my_dacorator
# def show():
#     print("this is main unction")

# show()


# # @my_dacorator
# # def againshow():
# #     print("this is new funcation")

# # againshow()





# # def xyz(e):
# #     print("this is value of e : ", e)

# # xyz(2384623948)

def my_dacorator(myfun):
    def wrappper(*args, **kwargs):
        print("welcom to my function..")
        
        myfun(*args, **kwargs)
        
        print("thank you for using my function :)")

    return wrappper


@my_dacorator
def xyz(a, b):
    c = a + b
    print("the sum is : ", c)

xyz(100, 200)
