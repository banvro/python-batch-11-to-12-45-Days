import tkinter as tk 

app = tk.Tk()
app.geometry("700x500")
app.title("this is my app")
app.config(background = "lightgreen")

lbl = tk.Label(app, text = "this is car", font = ("robort", 23, "bold"))

# lbl.pack()
# lbl.grid(row = 0, column = 100)

lbl.place(x = 300, y = 100)



app.mainloop()