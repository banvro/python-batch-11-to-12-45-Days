# 1) compile time error (syntex error)

# a =  10
# print(a)

# if 10 == 10
#     print("helloo")

# 2) logical errors 

# a = 10
# b = 0

# c = a/ b
# print(c)



# 3) run time error : 

# age = int(input("Enter your age : "))

# print(age)





# Erros : 
#         1) compile time error
#         2) logical error
#         3) run time error


# try:
#     # try thus code...

# except Exception:
#     # accept the errors

# else:
#     # execute only when try does't hanve any error

# finally:
#     # done
    

a = 10
b = 2

try:
    c = a / b
    age = int(input("Enter your age : "))

except ValueError:
    print("Enter valid age ...")

except ZeroDivisionError:
    print("You never devid anything with zeroooo")

except Exception as e:
    print("here is error")

else:
    print("user age is : ", age)

finally:
    print("exception hNDLING DONE...")
    
print("runningggg")










