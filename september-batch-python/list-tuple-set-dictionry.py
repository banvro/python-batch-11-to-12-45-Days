# List
# Tuple
# Set
# Dictionry

# to store multipal/ collection of data in a single variable


# List : Ordered, Allow Duplicate value, mutable (Changable)

# Tuple : Ordered, allow duplicasy, imutable

# Set : unordered, do not allow duplicasy, mutable

# dictiomnry : ordered, do not allow duplicasy, mutable

# List : Ordered, Allow Duplicate value, mutable (Changable)

# []

# lst = [100, 80, 30, "hello", 100.78, 90, 100]

# print(lst)
# print(type(lst))

# print(lst[3])

# print(lst[1] + lst[2])




# lst = [100, 80, 30, "hello", 100.78, 90, 100]

# slice :

# lst[start : end : increament]

# print(lst[2 : 6 : 2])

# print(lst[])






# lst = [100, 80, 30, "hello", 100.78, 90, 100]


# # print(lst[::])

# # print(lst[-1])

# print(lst[::-1])

# Mutable : 
# lst = [100, 80, 30, "hello", 100.78, 90, 100]


# to add new data
# 1) append()
# 2) insert()
# lst.append(2000)

# lst.insert(2, 2000)

# print(lst)

# lst = [100, 80, 30, "hello", 100.78, 90, 100]

# to delete data

# 1) pop()
# 2) remove()

# lst.pop()

# lst.remove(100)

# lst.remove(100)

# lst.remove(lst[-1])

# lst = [100, 80, 30, "hello", 100.78, 90, 100]


# lst.clear()

# print(lst)

# lst = [100, 80, 30, "hello", 100.78, 90, 100]


# zx = lst[::-1]

# print(zx)

# zx.remove(100)

# qw = zx[::-1]

# print(qw)

# abc = []



# for i in lst:
#     if i == lst[6]:
#         continue
#     abc.append(i)


# print(abc)












# Tuple : 
# Tuple : Ordered, allow duplicasy, imutable
# ()



# tpl = (12, 100, 90, 100.8, 100, "hello", "ok", 20)

# print(tpl)
# print(type(tpl))

# print(tpl[5:8])

# tpl = (12, 100, 90, 100.8, 100, "hello", "ok", 20)

# lst = list(tpl)

# print(lst)

# lst.append(2000)

# new = tuple(lst)

# print(new)





# Set : unordered, do not allow duplicasy, mutable
# {}

# st = {12, 20, 100, 78, "helo", "xyz", 100, 20}

# print(st)
# print(type(st))

# 1) add()

# st = {12, 20, 100, 78, "helo", "xyz", 100, 20}

# st.add(3000)

# 1) pop()
# 2) remove()
# st = {12, 20, 100, 78, "helo", "xyz", 100, 20}

# # st.pop()
# st.remove(12)
# print(st)







# dictiomnry : ordered, do not allow duplicasy, mutable
# {key : value }

# JSON = javascript object notation


# dic = {
#     "name" : "kriss",
#     "age" : 20,
#     "number" : 9823492864
# }

# print(type(dic))

# print(dic["age"])


# dict = {
#     1 :{
#         "name" : "kirss",
#         "age" : 20,
#         "number" :{
#             "number1" : 29834664,
#             "number2" : 9846594386
#         }
#     },

#     2 : {
#         "name" : "moris",
#         "age" : 93
#     }
# }




# dict = {
#     1 :{
#         "name" : "kirss",
#         "age" : 20,
#         "number" :{
#             "number1" : 29834664,
#             "number2" : 9846594386
#         }
#     },
#     2 : {
#         "name" : "moris",
#         "age" : 93
#     }
# }

# print(dict[1]["number"]["number1"])






# dic = {"name" : "kriss", "age" : 29}


# # dic["Address"] = "this is a address"

# dic.pop("age")

# print(dic)










