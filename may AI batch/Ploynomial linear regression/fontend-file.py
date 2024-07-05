import numpy as np
import joblib
import tkinter as tk
from sklearn.preprocessing import PolynomialFeatures

mymodel = joblib.load("icecreem_seeling_unit_predictor.joblib")

app = tk.Tk()

app.geometry("700x300")
app.config(background = "lightgreen")
app.title("Pretioner")

def check_slaes():
    tem = inp.get()
    tem = np.array(float(tem))
    tem = tem.reshape(-1, 1)
    ploy = PolynomialFeatures(degree = 2)
    data = ploy.fit_transform(tem)

    print(data[0], "xxxxxxxxxxxxxxxx")
    all_betas = mymodel.coef_
    my_interept = mymodel.intercept_
    print(all_betas)
    # y = b0 + b1x1 + b2x2 + b3x3

    y = my_interept + (all_betas[0]*data[0][0]) + (all_betas[1]*data[0][1]) + (all_betas[2]*data[0][2])


    lblshow.config(text = f"Ice Cream Sales (units) : {y}")


lbl = tk.Label(app, text = "Tempreture In Celcius", font = ("robort", 30, "bold"), foreground = "darkgreen", background = "lightgreen")
lbl.pack(pady = 20)

inp = tk.Entry(app, font = ("robort", 25), fg = "green")
inp.pack()

btn = tk.Button(app, text = "Check Sales", font = ("robort", 16, "bold"), background = "green", fg = "white", command = check_slaes)
btn.pack(pady = 20)

lblshow = tk.Label(app, text = "", font=("robort", 16, "italic"), fg = "green", background = "lightgreen")
lblshow.pack()

app.mainloop()