# tkinter => GUI, PyQT5

import tkinter as tk

def showme():
    zx = ent.get()
    print(zx)
    lblx.config(text = "hey how are you")


app = tk.Tk()
app.geometry("500x300")
app.title("this is a title")
app.config(background = "#a9fc6a")


lbl = tk.Label(app, text = "Hellow World", font = ("robort", 30, "bold"), fg = "red", bg = "#c8ebae")
lbl.pack(fill = "x", padx = 30, pady = 25, ipady=  10, side = "top")

ent = tk.Entry(app, font = ("robort", 20, "italic"))
ent.pack()

btn = tk.Button(app, text = "Submit", font = ("robort", 15), command = showme)
btn.pack(pady = 20)


lblx = tk.Label(app, text = "", font = ("robort", 10), fg = "blue", bg = "#a9fc6a")
lblx.pack()


app.mainloop()

# padding

# pack()
# grid()
# place()
