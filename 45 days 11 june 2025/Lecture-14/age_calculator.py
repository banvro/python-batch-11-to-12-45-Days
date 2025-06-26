import tkinter as tk 

def calculateage():
    xy = agee.get()
    age = int(xy)
    new_age = 2025 - age
    
    showinfo.config(text = f"Your are {new_age} years old.")


app = tk.Tk()

app.geometry("900x400")
app.title("Age Calculator")
app.config(background = "#2ff7c9")

xyz = tk.Label(app, text = "Age Calculator", fg = "#2ff7c9", bg = "#12a180", font = ("robort", 45, "bold"))
xyz.pack(fill = "x", ipady = 10)

agee = tk.Entry(app, font = ("robort", 32, "italic"), bg = "#b1f0e1", fg = "#139c7b")
agee.pack(pady = 35)


btn = tk.Button(app, text = "Check Age", fg = "#2ff7c9", bg = "#12a180", font = ("robort", 24, "bold"), command = calculateage)
btn.pack(ipadx = 23)


showinfo = tk.Label(app, text = "", bg = "#2ff7c9", font = ("robort", 20), fg = "#0f8a6c")
showinfo.pack(pady = 30)

app.mainloop()