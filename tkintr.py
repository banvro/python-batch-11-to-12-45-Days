# # Tkinter :  python GUI Library

# import tkinter as tk

# def showm():
#     print("okkkkkkk   xyz")

# root = tk.Tk()

# root.geometry("500x500")
# root.title("My Tkinter")
# root.configure(background = "green")

# lebl = tk.Label(root, text = "this is my text", font = ("Roboto", 20, "bold"), fg = "red", bg = "yellow")
# # 1) pack()
# # 2) grid()
# # lebl.pack(fill = "x", padx=20, pady=30, ipadx=20, ipady= 30, side=tk.LEFT)
# lebl.pack(fill = "x", padx=20, pady=30, ipadx=20, ipady= 30)

# entery = tk.Entry(root)
# entery.pack(ipady=20)

# btun = tk.Button(root, text = "click me", command = showm)

# btun.pack(pady = 20)

# root.mainloop()


import tkinter as  tk

def getinfo():
    # print("yyyyyyyyyyyyy")
    nam = entr1.get()
    xyz = entr2.get()

    print(nam, xyz)


root = tk.Tk()
root.geometry("400x400")

labl = tk.Label(root, text = "Enter Name : ")
lab2 = tk.Label(root, text = "Enter p.no : ")
entr1 = tk.Entry(root)
entr2 = tk.Entry(root)
btn = tk.Button(root, text = "submit", bg = "red", fg = "white", command=getinfo)

labl.grid(row=1, column=1, padx=15, pady=5)
entr1.grid(row=1, column=2, padx=15, pady=5)

lab2.grid(row=2, column=1, padx=15, pady=5)
entr2.grid(row=2, column=2, padx=15, pady=5)

btn.grid(row=3, column=2)


root.mainloop()