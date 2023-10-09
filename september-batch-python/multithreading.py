# # multithreading : 

# a = 10
# b = 200

# c = a + b

# print(c)

# print("hello")

# print("running...")


# print("done")

import threading

def fun1():
    for i in range(100):
        print("Hellooooo")

def fun2():
    for i in range(100):
        print("nooooooooo")

print("strat code,....")

# fun1()
# fun2()


th1 = threading.Thread(target = fun1)
th2 = threading.Thread(target = fun2)

th1.start()
th2.start()

print("hello world")

print("i am importtant code")

print("runninggg...")

th1.join()
th2.join()

print("i a done")





# a = 10
# b = 20

# c = a + b


# d = c + 20

# print(d)