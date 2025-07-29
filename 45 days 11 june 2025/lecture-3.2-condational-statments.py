# Operators:


# Control Statments:
#     are those statments which control the flow of execution of a program.

# Condational Statments:

# if, elif, else

# Syntax


# condation ----> compersion operators

# if condation:
    # block of code...
    

# space ---> indentation

# x = 200

# if x > 100:
#     print("the value of x is bigger then 100")


# print("heyyyyyyyy!")




# if condation:
#     # block of code....

# else:
#     # block of code...



# Voating System


# print("******** My Voating System ********")
# print()

# age = int(input("Enter your age : "))


# if age > 18:
#     print("you are eligible for voat")

# else:
#     print("you are not eligible for voat")



# elif
    # --> when we have more then 1 condations----


# print("%%%%%% Welcom to my Voating System &&&&&&&")

# print()

# age = int(input("Enter your age : "))

# if age > 18:
#     print("You are eligible for voat")
    
# elif age == 18:
#     print("Welcome!this is your first voat")
    
# elif age == 19:
#     print("This is your second Voat")

# else:
#     print("you are not eligible for vaot")



# Problem: Get a input from user and check the number is even or odd.


# num = int(input("Enter a number : "))

# if num % 2 == 0:
#     print("Entered number of even")

# else:
#     print("number is odd")




# Design a calculator

#  ************ my Calculator ************


# num1 = ?
# num2 = ?

# ::::::Choices:::::

#     1) Adation
#     2) Subtration
#     3) Multiplication
#     4) Devsion

# chice = ?3

print("******** My Calculator ***********")
print()

num1 = int(input("Enter first number : "))
num2 = int(input("ENter second number : "))

print("""
      :::::::::: Choices are :::::::::::
      1) Adation
      2) Subtration
      3) Mutiplication
      4) Devsion
""")

print()
choice = int(input("What you wana do : "))

if choice == 1:
    zx = num1 + num2
    print("The sum is :", zx)

elif choice == 2:
    zx = num1 - num2
    print("The Subtration is :", zx)

elif choice == 3:
    zx = num1 * num2
    print("The multiplicion is :", zx)

elif choice == 4:
    zx = num1 / num2
    print("The devsion is :", zx)

else:
    print("ENter a valid key...!")
