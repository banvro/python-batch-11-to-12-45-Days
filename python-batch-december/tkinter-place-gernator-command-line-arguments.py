# import tkinter as tk

# app = tk.Tk()
# app.geometry("400x400")

# lbl = tk.Label(app, text = "heyyyyyyyyy", font = ("robort", 16, "bold"))
# # lbl.pack()
# # lbl.grid(row = 0, column = 100)

# lbl.place(x = 0, y = 400)


# app.mainloop()




# import sys 


# print("welcom ", sys.argv[1] ,". you are the employe of ", sys.argv[2])


# gernator

# GENERATORS

# def xyz():
#     for i in range(1, 10):
#         print(i)


# y = xyz()

# print(y)




# def xyz():
#     for i in range(1, 10):
#         print(i)

# yield


# def xyz():
#     yield 1
#     yield 2
#     yield 3

# # print(xyz())
# x = xyz() 

# print(next(x))
# print(next(x))
# print(next(x))

def hey():
    for i in range(1, 10):
        yield i


y = hey()

print(next(y))
print(next(y))
print(next(y))
print(next(y))
