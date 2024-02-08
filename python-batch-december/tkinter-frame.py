import tkinter as tk

app = tk.Tk()

app.geometry("400x600")
app.title("Learn Frame")
app.config(background = "yellow")

frame1 = tk.Frame(app, background = "white", border = 20, relief = "sunken")
frame1.pack(fill = "x")

fran2 = tk.Frame(app, background = "pink", border = 20, relief = "groove")
fran2.pack(fill="x")

lbl = tk.Label(frame1, text = "Hellow world", font = ("robort", 30, "bold"), fg = "red", bg = "white")
lbl.pack(pady = 20)

lbl1 = tk.Label(fran2, text = "Name : ", font = ("robort", 15, "bold"), fg = "red", bg = "pink")
lbl1.grid(pady = 20, row = 0, column = 0)

entr = tk.Entry(fran2, font = ("robort", 15, "bold"))
entr.grid(row=0, column=1)





app.mainloop()
