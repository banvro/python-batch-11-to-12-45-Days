# Condational Statments:
#     # ------------------------
    
    
# Loops:
#     ittrations / repetation
    
#     Types:
#         1) For loop
#         2) while loop


# 1) For loop:
#     ---> ittrable object ---> data
#         ----> one by one


# Syntax:
    
# for veriable_name in objeact_name:
#     code .....



# zx = "this is a car"

# for x in zx:
#     print(x)




# xyz = "hello"

# for i in xyz:
#     print(i)
#     print("eeeeeeeeeeeee")
#     print(i, i, i, i, i, i)
#     print("ok")

# print("done")


# abc = "abcdefghi"

# for i in abc:
#     print("i")


# x = 122345

# x = str(x)

# for z in x:
#     print(z)


x = 122345

# x = str(x)

# for z in x:
#     print(z, end = " ")


# range()
#     ---> help us to genrate data from one location to another


# range(start, end, incremet)
    
#     default values:
#         start ---> 0
#         end ---> n - 1
#         increment --> 1
    

# for i in range(1, 20, 1):
#     print(i)


# for z in range(3, 10):
#     print(z)


# for i in range(1, 20, 2):
#     print(i)

# Problem:

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# .
# .
# .
# 2 x 10 = 20


# for i in range(1, 11):
#     print("2 x", i, "=", 2*i)


# for i in range(1, 11):
#     print(f"2 x {i} = {2*i}")



# problem:

# 10 x 1 = 3
# 9 x 2 = 6
# 8 x 3 = 9
# 7 x 4 = 12
# 6 x 5 = 15
# .
# .
# .
# 1 x 10 = 30


# for i in range(1, 11):
#     print(11-i, "x", i, "=", 3*i)



# print("h" * 3)

# a 
# a a
# a a a
# a a a a
# a a a a a
# a a a a a a

# for i in range(1, 7):
#     print("a " * i)



# x = "this is a car and this is a good car"


# for i in x:
    
#     if i == "a":
#         print("hello")
#     else:
#         print(i)

# problem:
#     fizzbuzz


# 1 -------------> 50

# multiple of 3 ----> fizz

# multiple of 5 ---> buzz

# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz


# for i in range(1, 51):
    
#     if i % 3 == 0:
#         print("fizz")
    
#     elif i % 5 == 0:
#         print("buzz")
    
#     else:
#         print(i)


# veriables handeing


# zx = "1286319301000020002000"

# x = 0

# for i in zx:
    
#     if i == "0":
#         x = x + 1

# print(x)



# x = "this"

# q = 0

# for i in x:
#     q = q + 1 # 4

# print(q)


# x = inout()
#     ---> this is a car r


# vovles

# a --> 5
# e
# i
# o
# u

# x = input("Enter you text : ")

# a_count = 0
# e_count = 0
# i_count = 0
# o_count = 0
# u_count = 0
# other = 0

# for i in x:
#     if i == "a":
#         a_count = a_count + 1
#         # a_count += 1
#     elif i == "e":
#         e_count = e_count + 1
        
#     elif i == "i":
#         i_count = i_count + 1
        
#     elif i == "o":
#         o_count = o_count + 1
        
#     elif i == "u":
#         u_count = u_count + 1

#     else:
#         other = other + 1



# print(f"""
# a ---> {a_count}
# e ---> {e_count}
# i ---> {i_count}
# o ---> {o_count}
# u ---> {u_count}
# other ---->{other}
# """)



# Nested for loop----


# for j in range(1, 11):
#     print(j, "eeeeeeeeeeeeeeeee")
#     for i in range(1, 5):
#         print(i)





# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()















