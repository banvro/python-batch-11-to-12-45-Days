# WHILE LOOP => its ittrate for when our condation is true

# a = 1

# # 10 == 10

# while a < 10:
#     # print("hello, this is me....")
#     a = a + 1

#     print(a)





a = 1

# 10 == 10

# while a < 10:
#     # print("hello, this is me....")
#     print(a)
#     a = a + 1

# while True:
#     if a < 10:
#         a = a + 1
#         print(a)



# lt = [1, 2,3 , 4, 5]

# # to add new element in list we use append

# lt.append("bus")

# print(lt)

lt = []
while True:
    wish = input("Press q for quit or a for add new name : ")
    # a == q
    if wish == "q":
        break
    # a == a
    elif wish == "a":
        usernme = input("Enter new name : ")
        lt.append(usernme)
        print(lt)
    else:
        print("something went wrong..")
        break
        
    
# print(list)











