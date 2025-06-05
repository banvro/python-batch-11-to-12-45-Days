import tkinter as tk

app = tk.Tk()
app.geometry("1000x500")
app.title("This is my first app")
app.config(background = "#1bff0a")

lbl = tk.Label(app, text = "Hellow word", font = ("Robort", 45, "bold"), fg = "lightgreen", bg = "green")
lbl.pack(fill = "x", pady = 30, padx = 30, ipady = 5, side = "top")

ent = tk.Entry(app, font = ("robort", 38), bg = "lightgreen")
ent.pack()

bn = tk.Button(app, text = "i am button", bg = "darkgreen", fg = "lightgreen", font = ("robort", 27, "bold"))
bn.pack(pady = 30, ipadx = 50)


app.mainloop()