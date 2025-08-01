# for loop

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9

# for i in range(1, 10):
#     print((str(i) + " ") * i)



# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# for i in range(5, 0, -1):
#     print((str(i) + " ") * i)


# 1 2 3 4 5
# 1 2 3 4
# 1 2 4
# 1 2
# 1

# for i in range(5, 0, -1):
#     # print(i, "-------------")
#     for j in range(1, i + 1):
#         print((str(j) + " "), end = "")
#     print()


# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4 
# 5



# for i in range(10, 1, -1):
#     print(i)



# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4 
# 5

# for i in range(5, 0, -1):

#     for j in range(5, 5 - i, -1):
#         print(str(j) + " ", end = "")
#     print()



#           1
#         1 1
#       1 1 1
#     1 1 1 1
#   1 1 1 1 1
# 1 1 1 1 1 1



for i in range(1, 7):
    print((6 - i) * "  ", i * ("1" + " "))


          1
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5
1 2 3 4 5 6



