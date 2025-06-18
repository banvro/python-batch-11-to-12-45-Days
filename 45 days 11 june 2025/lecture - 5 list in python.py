# Data Sructures:
    
#     Python:
#         1) List
#         2) Tuple
#         3) set
#         4) dictionry
        
        
# a = 10

# name = "hellow owlrd"



# List::
#     is a spacial type of data type help us to store multiple elemnts in a single veribale.
    
# []

# list ---> hittrogenious (diffrent type)

# lst = [12, 10, 34, 100, 10.4, "hello"]

# print(lst)

# print(type(lst))


# list --->
#     key points:
#         1) ordered
#         2) hold duplicate data
#         3) Mutable ---> (modify)


# 1) ordered
#     ---> sequence
#         ---> indexing, slicing


# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9]

# print(zx[6])


# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9]

# print(zx[-3])


# Slicing:
#     --> 

# [statrt : end : incremnt]

# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9]


# print(zx[1 : 5])


# print(zx[3 : 8])


# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9, 34, 6]

# print(zx[0 : 11 : 2])



# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9, 34, 6]

# print(zx[2 : ])

# print(zx[5 : ])


# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9, 34, 6]


# print(zx[ : 4])

# [start_index  :  end_inedx  : incremt]

# zx = [12, 34, 5, 7, 8, 45, 67, 8, 9, 34, 6]


# print(zx[ : : -1])


# x = [12, 34, 12, 23, 4, 12]

# print(x)


# 3) Mutable 
#     ---> able to chnage list after create

# Modify ---> adding new data
#         ---> replace
#         ---> delete



# lt = [12, "hello", 200, 10, "90"]

# # 1) adding data in list

# 1) append()
#     ---> to add data at the end location in a list.

# 2) insert()
#     ---> help to add data at a prticuler location.

# print(lt)




# append()

# syntax:
    
# list_name.append(new_data)

# lt = [12, "hello", 200, 10, "90"]

# lt.append(1000)

# lt.append("hellooooooo")

# print(lt)



# Problem:

# x = []

# for ---> 1 to 20

# output:

# [1, 2, 3, 4, 5, ........, 20]


# x = []

# for i in range(1, 21):
#     x.append(i)
    
# print(x)


# [1, 22, 3, 4444, 5, 666666, 7, 88888888, 9]


# y = []

# for i in range(1, 10):
    
#     if i % 2 == 0:
#         y.append(int(str(i) * i))
#     else:
#         y.append(i)

# print(y)


# ["2 x 1 = 2", "2 x 2 = 4", "2 x 3 = 6", ..........]


# tbl = []

# for i in range(1, 11):
#     zx = f"2 x {i} = {2*i}"
#     tbl.append(zx)

# print(tbl)




# 2) insert()
#     ---> add eleent at a prticyler lpcation
    
# Syntax:

# list_name.insert(index_number, new_element)


# zx = [12, 3, 4, 5, 6, 7, 8, 45]

# zx.insert(2, 1000)

# print(zx)


# zx = [12, 3, 4, 5, 6, 7, 8, 45]

# zx.insert(-2, 2000)

# print(zx)



# Deleting lemnts from list

# 1) pop()

# 2) remove()

# 3) delete


# 1) pop()
#     ----> to delete last element from a list


# syntax:

# list_name.pop()

# pq = [12, 3, 5, 6, 767, 89, 67, 45]

# pq.pop()

# pq.pop()

# print(pq)


# remove()

# syntax:

# list_name.remove(elemt)



# x = [12, 4, 5, 6, 7, 8, 5, 34, 3, 23]


# x.remove(34)

# # x.remove(5)




# del x[0]

# print(x)




# replace

# zx = [23, 5, 7, 8, 9, 56, 45]

# zx[4] = 9000

# print(zx)



# x = ["this is a car", "this is a bus"]

# y = x[0]

# print(y[9:])




# sort()


# zx = [12, 34, 45, 6, 8, 9, 6, 45,  1, 23]

# zx.sort()

# print(zx[::-1])


# x = [1, 2, 3]

# y = [2, 3, 4, "helooo"]

# x.extend(y)


# print(x)






# clear()

# zx = [12, 23, 45, 56, 78, 89, "hhep", 3]

# zx.clear()

# print(zx)


zx = [12, 23, 45, 56, 78, 89, "hhep", 3]



print(zx.index("hhep"))










