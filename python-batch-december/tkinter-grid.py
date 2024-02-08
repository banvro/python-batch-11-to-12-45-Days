import tkinter as tk

app = tk.Tk()
app.geometry("700x500")
app.title("Learn Grid")
app.config(background = "yellow")

lbl = tk.Label(app, text = "", font = ("robort", 20, "bold"))
lbl.grid(row = 0, column = 0, padx=30)

lbl = tk.Label(app, text = "Hello", font = ("robort", 20, "bold"))
lbl.grid(row = 1, column = 1, pady=20)

ent = tk.Entry(app, font = ("robort", 20, "italic"))
ent.grid(row = 1, column= 2)

lblx = tk.Label(app, text = "Seond column", font = ("robort", 20, "bold"))
lblx.grid(row = 2, column = 1)

ent1 = tk.Entry(app, font = ("robort", 20, "italic"))
ent1.grid(row = 2, column= 2)

app.mainloop()
