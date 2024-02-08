# # Duck Typing:
    
# class car:
#     def tyers(self):
#         print("this have 4 small typer")
    
#     def hight(self):
#         print("the hight is small")
    
#     def seats(self):
#         print("miximum 4 to 6 seats")
    
# class train:
#     def tyers(self):
#         print("this have 550 to 600")
    
#     def hight(self):
#         print("the grate is small")
    
#     def seats(self):
#         print("miximum 120 to 600 seats")
        
        
# obcar = car()
# obtrain = train()

# def vichical(x):
#     x.tyers()
#     x.hight()
#     x.seats()
    
# vichical(obtrain)





# Exception handeling:

# Types of Errors:
#     1) Compile Time Error
#     2) Logical Error
#     3) Run Time Error

#     1) Compile Time Error (syntex Error)

# a = 10
# b  20
# c = a + b
# print(c)



# if 100 == 100
#     print("this is 100")


# 2) Logical Error:

# a = 100
# b =  0

# c = a / b

# print(c)


# 3) Run time Error:

# age = int(input("Enter Your Age : "))



# Exception handling:


# a = 10
# b  20
# c = a + b

# print(c)

# print("i am impoertant code")

# print("woring")

# print("done....")

# try:
#     # doutable code.....
    
# except Exception:
#     # when try get an any error

# else:
#     # try do not have any errorrr

# finally:
#     # it just indecate exception handeling done...


a = 10
b = 0

try:
    c = a / b

except Exception as e:
    print(e)

else:
    print("the devsion of a and b is  : ", c)
    
finally:
    print("this is finally block..")

print("hello")
print("doneee")

class done !
