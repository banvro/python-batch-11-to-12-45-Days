# import re

# txt = "this is a car. this is a bus. is this a bus... car"

# ptrn = "car"

# # xyz = re.findall(ptrn, txt)

# # print(xyz)

# xyz = re.sub(ptrn, "airoplain", txt)

# print(xyz)

# MultiThreading

# def fun1():
#     for i in range(1, 100):
#         print("helllooooo")
    
# def fun2():
#     for i in range(1, 100):
#         print("nooooooo")

# fun1()
# fun2()

# print("helloooo")
# print("i am importtant code")

# print("gooooo")

# print("done")



import threading

def fun1():
    for i in range(1, 100):
        print("helllooooo")
    
def fun2():
    for i in range(1, 100):
        print("nooooooo")

# fun1()
# fun2()
        
th1 = threading.Thread(target = fun1)
th2 = threading.Thread(target = fun2)

th1.start()
th2.start()

print("helloooo")
print("i am importtant code")

print("gooooo")

th1.join()
th2.join()

print("done")



# word

# process : 
# thred : 


# pri


# a = 10
# b = 20

# c = a + b

# print("goooooo")

# d = c + 2000

# print(d)
