# GUI

import tkinter as tk
import joblib
import numpy as np

model = joblib.load("Cgpa_Predictor.joblib")

def predictpkg():
    cgpa = float(ent.get())
    cgpa = np.array(cgpa)
    cgpa = cgpa.reshape(1, -1)
    x = model.predict(cgpa)
    x = x[0]
    zx = str(x)
    
    lbshow.config(text = f"Your Package is : {zx[:4]} lpa.")

    ent.delete(0, tk.END)

app = tk.Tk()
app.geometry("600x350")
app.title("This is my title")
app.config(background="#70ed09")

lbl = tk.Label(app, text = "Pkg Predictor", font = ("Robort", 35, "bold"), fg = "red", bg = "#faec55")
lbl.pack(fill="x", side="top", pady=20, padx=20, ipady=10)

ent = tk.Entry(app, font = ("Robort", 28))
ent.pack()

btn = tk.Button(app, text = "check", font=("Robort", 20, "bold"), fg = "white", bg = "green", command=predictpkg)
btn.pack(pady=20, ipadx=20)

lbshow = tk.Label(app, text="", font  =("Robort", 16), bg="#70ed09")
lbshow.pack()

app.mainloop()


# pack()
# grid()
# place()


