# Functions 

# 1) lambda
# 2) map()
# 3) filter()
# 4) reduce()
# 5) comperhenstion


# def xyz(a, b):
#     c = a + b
#     print(c)

# xyz(10, 20)



# lambda 


# zx = lambda arguments : experssion

# zx = lambda a, b : a + b

# print(zx(100, 200))

# print(zx(1, 2))



# sq = lambda a : a ** 2 + 10

# print(sq(3))



# map() 

# lst = [2, 4, 1, 6, 5, 10, 7, 6]

# # map(lambda, ittrater)

# zx = map(lambda i : i - 10, lst)

# print(list(zx))




# filter()

# filter(function, ittrater)

# zx =  [2, 6 ,1, 3, 4, 7, 9, 1, 3, 5]


# for i in zx:
#     if i % 2 != 0:
#         print(i)

# qw = filter(lambda i : i % 2 != 0, zx)

# print(tuple(qw))


# reduce()


# from functools import reduce

# reduce(function, itrater)
# lst = [1, 2, 57, 12, 9, 10, 6, 4, 1]
# l = 0

# for i in lst:
#     l = l + i

# print(l)



# from functools import reduce

# lst = [1, 9, 57, 1, 9, 10, 6, 4, 1]

# we = reduce(lambda a, b : a + b, lst)

# print(we)




# COMPREHENSIONS 

# use to genrate data, list, tuple, set

# lst = [expression loop condation]

# lst = [i + 2 for i in range(20) if i % 2 != 0]

# print(lst)

def xyz(*args):
    z = 0
    for i in args:
        z = z + i
    print(z)


# xyz(1, 2, 36, 1)
e = int(input("ENter how many numbers your want to enter : "))

lst = [int(input(f"Enter {i + 1} number : ")) for i in range(e)]

# print(lst)

xyz(*lst)







