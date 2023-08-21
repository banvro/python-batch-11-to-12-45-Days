# a = 10

# b = 20

# c = a + b

# for i in range(1200):
#     print(i)


# print(c)

import threading


class myclass:
    def runthisfirst(self):
        for i in range(100):
            print("hello..................")
    
    def nowrunthis(self):
        for i in range(100):
            print("nooooooo....")


obj = myclass()

# obj.runthisfirst()
# obj.nowrunthis()

th1 = threading.Thread(target = obj.runthisfirst)
th2 = threading.Thread(target = obj.nowrunthis)

th1.start()
th2.start()

print("i am ruuning.....")

print("i am importtant")

th1.join()
th2.join()

print("done")