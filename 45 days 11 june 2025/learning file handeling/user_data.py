print("------ Storee your  persnonal info ---------")

file = open("userdata.txt", "a")

name = input("Enter youur name : ")
age = input("ENter your age : ")
phone_num = input("Enter your phone number : ")
email = input("ENter your emai address : ")

file.write(f"\n{name} ----  {age} --- {phone_num} ---- {email}")

file.close()



