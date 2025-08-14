
# open() ----> file handeling

# mode -----> control file (open, write, read)


# mode -----> reading a text file 


# fl = open("hlo.txt", "r")

# print(fl.read())

# print(fl.readline())
# print(fl.readline())
# print(fl.readline())

# properties:
#     1) to read files we use r mode 
#     2) if file is not exist ---> error


# x = open("xyz.txt", "r")


# --------------------------------------------------------------

# write mode ----> w

file = open("xyz.txt", "w")
file.write("heyyyyyyyyyy!")
file.close()

# --> it create a new file if file does't exist.
# ---> it erase old data 


# --------------------------------------------------------------

# append mode ----> a 

# -----> it create a new file if file is not exist .
# ----> it also hold the previous data.


file = open("userinfo.txt", "a")
file.write("\nthis heyyyyyy! ok")
file.close()