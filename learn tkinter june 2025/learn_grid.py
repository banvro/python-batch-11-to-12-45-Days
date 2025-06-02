import tkinter as tk

app = tk.Tk()
app.geometry("800x600")
app.config(background = "skyblue")


lbl = tk.Label(app, text = "Full Name", font = ("robort", 20, "bold"), bg = "skyblue")
lbl.grid(row = 0, column = 0)

lblx = tk.Label(app, text = ":", font = ("robort", 20, "bold"))
lblx.grid(row = 0, column = 1, pady = 20, padx = 10)

ent = tk.Entry(app, font = ("robort", 20, "bold"))
ent.grid(row = 0, column = 2)



lbl1 = tk.Label(app, text = "Phone Number", font = ("robort", 20, "bold"))
lbl1.grid(row = 1, column = 0)

lbl2 = tk.Label(app, text = ":", font = ("robort", 20, "bold"))
lbl2.grid(row = 1, column = 1)

ent1 = tk.Entry(app, font = ("robort", 20, "bold"))
ent1.grid(row = 1, column = 2)


x = tk.Text(app, height = 8, width = )
x.grid(row = 3, column = 2)

app.mainloop()