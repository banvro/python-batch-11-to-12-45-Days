import tkinter as tk 
from datetime import datetime, date

# day-month-year

def calculate_age():
    x = age.get()

    proper_dob = datetime.strptime(x, "%d-%m-%Y").date()

    current_time = date.today()

    yearss = current_time.year - proper_dob.year
    month = current_time.month - proper_dob.month
    days = current_time.day - proper_dob.day
    
    lblshow.config(text = f"You are {yearss} years, {month} months and {days} Days old.")
    

app = tk.Tk()

app.geometry("900x400")
app.title("Age Calcualtor")
app.config(background = "#64ff21")

lbl = tk.Label(app, text = "Age Calculator", font = ("robort", 45, "bold"), bg = "#277a02", fg = "#a5f781")
lbl.pack(fill = "x", pady = 30, padx = 30, ipady = 5)

age = tk.Entry(app,  font = ("robort", 30, "bold"), bg = "#A2FF7A", fg = "#000000")
age.pack()

btn = tk.Button(app, text = "Check Age", font = ("robort", 23, "bold"), bg = "#277a02", fg = "#a5f781", command = calculate_age)
btn.pack(pady = 30)


lblshow = tk.Label(app, text = "", font = ("robort", 20), fg = "#236705", background = "#64ff21")
lblshow.pack()

app.mainloop()