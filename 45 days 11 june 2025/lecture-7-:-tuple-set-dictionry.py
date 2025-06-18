# Data Structure:
    
#     List:
#         1) ordered
#         2) allow duplicate data
#         3) Mutable (modify)
        
# 2) tuple:
#     1) ordred
#     2) allow duplicate data
#     3) immutable
    
# ()

# zx = (12, "hello", True, "12.0")

# print(zx)

# print(type(zx))



# ordered ---> sequence

# ---> indexing, slicing



# zx = (12, 34, 45, "hello", 67, 100)

# print(zx[4])

# print(zx[-1])



# x = (12, 34, 45, 12, 12, 12, 34, 45)


# print(x)



# 3) immutable


# List      |    tuple


# []        |    ()

# mutable    |   imutable  





# 3) set:
    # 1) unordred
    # 2) do not allow duplicate data
    # 3) mutable

# {}


# st = {10, 20, "hello", "hello", 10, 45, 10}

# # print(type(st))

# print(st)


# 3) mutable ---->  modify



# x = {12, 34, 45, 67, 78}

# adding new element:

# add()
#     ---> help us to add new elemtn in set


# set_name.add(new_elemt)

# x.add(1000)

# print(x)


# delete element from set

    # 1) pop()
    # 2) remove()


# x = {12, 34, 45, 67, 78}

# 1) pop()
#     --> delete any random elemt

# x.pop()

# 2) remove()
#     ---> delete a prticuler element

# x.remove(78)

# print(x)




# set 
#     ---> 10th


# x = {12, 34, 45, 56, 7, 89}

# y = {12, 34, 5, 6, 7, 45, 2, 23, 12}

# # union

# z = x.union(y)

# print(z)

# # intersection

# zx = x.intersection(y)
# print(zx)

# # diffrence

# pq = y.difference(x)
# print(pq)


# 4) Dictriony:
#     1) ordred
#     2) do not allow duplicate data
#     3) mutable


# {key : value, key : value.....}



# info = {"name" : "Kriss Moris",
#         "age" : 21,
#         "phone_number" : 9286348263,
#         "email" : "krissmoris@gmail.com"
# }

# print(type(info))
# print(info)


# info = {"name" : "Kriss Moris",
#         "age" : 21,
#         "phone_number" : 9286348263,
#         "email" : "krissmoris@gmail.com"
# }


# print(info["email"])

# print(info.keys())

# print(info.values())



# info = {"name" : "Kriss Moris",
#         "age" : 21,
#         "phone_number" : 9286348263,
#         "email" : "krissmoris@gmail.com",
#         "age" : 20
# }

# print(info)




# mutable

# addding new data --> no function

# syntax

# dict_name[new_key] = new_value


# info = {"name" : "Kriss Moris",
#         "age" : 21,
#         "phone_number" : 9286348263,
#         "email" : "krissmoris@gmail.com",
# }

# info["address"] = "this is address"

# print(info)




# delete data:

# pop()


# info = {"name" : "Kriss Moris",
#         "age" : 21,
#         "phone_number" : 9286348263,
#         "email" : "krissmoris@gmail.com",
# }

# info.pop("phone_number")


# print(info)





# json --> javascript object notation

# ---> dict



# stu_info = {
#     101 : {
#         "name" : "python",
#         "age" : 12,
#         "number" : {
#             "own" : 923648634,
#             "p_num" : 29836498
#         }
#     },
#     102 : {
#         "name" : "java",
#         "age" : 21,
#         "number" : { 
#             "own" : 748234344,
#             "p_num" : 982639868
#             }
#     },
#     103 : {
#         "name" : "ruby", 
#         "age" : 20,
#         "number" : {
#             "own" : 92836498234,
#             "p_num" : 9283649832
#         }
#     }
# }



# print(stu_info[102]["number"]["p_num"])



# zx = [12, 34, 45, 56, [23, 4, 45], 100]

# print(zx)

# print(zx[4][1])



# zx = {
#     "color" : ["orange", "blue", "black"],
#     "fvrt" : ["yes", "no", "yes"]
# }

# print(zx["color"])


# problem

# dictionry :
#     {
#         1 : [1, 2, 3, 4, 5],
#         2 : [2, 4, 6, ]
        
#         .
#         .
#         .
#         10 : [10, 20,......]
#     }


# 2) 

# zx = [1, 2, 2, 3, 1, 2, 2, 3, 4, 4, 5, , 3, 3, 4, 4, 5, 6, 4, 3, 2, 2]

# {
#     1 : 5, 2 : 2, 
# }


# table = {}

# for i in range(1, 11):
#     tbl = []
    
#     for j in range(1, 11):
#         tbl.append(i*j)
    
#     table[i] = tbl

# print(table)




# zx = [1, 2, 2, 3, 1, 2, 2, 3, 4, 4, 5, , 3, 3, 4, 4, 5, 6, 4, 3, 2, 2]

# {
#     1 : 5, 2 : 2, 
# }

zx = [1, 2, 2, 3, 1, 2, 2, 3, 4, 4, 5, 3, 3, 4, 4, 5, 6, 4, 3, 2, 2]



dic = {}

for i in zx:
    dic[i] = zx.count(i)

print(dic)


---------------------------------------


# functions






