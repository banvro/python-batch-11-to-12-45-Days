import tkinter as tk
import joblib
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

myModel = joblib.load("icrecrem_seals_predoictor.joblib")

def checkPrediction():
    tmepx = ent.get()
    temp = float(tmepx)

    np_inp = np.array(temp)

    ploy = PolynomialFeatures(degree = 2)
    new_inp = ploy.fit_transform([[np_inp]])
    
    sales = myModel.predict(new_inp)

    lbshow.config(text = f"Your Seals is : {sales[0]}")

app = tk.Tk()


app.geometry("700x350")
app.title("Icrecrem unit predictor")
app.config(background = "#24f2c9")


lbl = tk.Label(app, text = "Enter Temprature (C*)", font = ("robert", 30, "bold"), bg = "#5af218", fg = "#1d7d6a")
lbl.pack(fill = "x", pady = 20, side = "top", padx = 10, ipady = 12)

ent = tk.Entry(app, font = ("robert", 27))
ent.pack()

btn = tk.Button(app, text = "Check Seals", font = ("robert", 23, "bold"), bg = "#000000", fg = "#ffffff", command = checkPrediction)
btn.pack(pady = 20)

lbshow = tk.Label(app, text = "", font = ("robert", 19), bg = "#24f2c9", fg = "black")
lbshow.pack()


app.mainloop()