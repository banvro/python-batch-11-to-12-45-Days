# Perameters:
#     1) POstioanl peramters
#     2) Keyword arguments
#     3) Default Perameters
#     4) Veriable length peramters
#         1) *args
#         2) **kwargs


# def sumthis(a, b):
#     print(a, b)
#     zx = a + b
#     print("the sun is : ", zx)

# sumthis(b = 12, a = 10)


# def sumthis(a = 0, b = 0):
#     c = a + b
#     print(c)

# sumthis(12, 90)


# 4) Veriable length peramters
#         1) *args
#         2) **kwargs


# def sumthis(*data):
#     totle = 0
#     for i in data:
#         totle = totle + i
    
#     print(totle)
    
# sumthis(12, 10, 20, 45, 34, 23, 12, 100, 1)



# def savedata(**data):
#     for key, value in data.items():
#         print(key, value)

# savedata(name = "kriss", age = 20)


# return : 

# def xyz(a, b):
#     c = a + b
#     return c


# zx = xyz(12, 10)

# print(zx)




# def hey():
#     return "hello world"


# print(hey())

# x = hey()

# print(x)




# Comperhension : 

# 1) list
# 2) dictionry
# 3) set


# lst = [12, 10, 20]

# [expresssion for loop condation]

# zx = [i for i in range(1, 21) if i % 2 != 0]

# print(zx)


# x = [f"2 x {h} = {2*h}" for h in range(1, 11)]

# print(x)






1)
a = ("name", "age", "number")
b = ["kriss", 20, 98263838693]

output:
    {"name" : "kriss", "age" : 20, "number" : 98263838693 }

2) 
zx = ["12", "car", 12, 30, "hey", 10, "no"]

output:
["!2", "car", "hey", "no"]
[12, 30, 10]


3) 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output:
[5, 4, 3, 2, 1, 10, 9, 8, 7, 6]


4) 
zx = ["name", "kriss", "age", 20, "number", 298364294]

output:
    {"name" : "kriss", "age" : 20, "number" : 98263838693 }


5) 

