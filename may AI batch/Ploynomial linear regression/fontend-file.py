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
    temp = float(inp.get())

    array_temp = np.array(temp)
    reshape_temp = array_temp.reshape(-1, 1)

    ploy = PolynomialFeatures(degree = 2)

    modifyed_temp = ploy.fit_transform(reshape_temp)
    print(modifyed_temp)
    # print(f"""
    #       original temo : {reshape_temp}
    #       modifyed tem : {modifyed_temp}""")

    beats = mymodel.coef_
    intercet = mymodel.intercept_

    print(f"""
          beats are : {beats}, 
          intercet is : {intercet}""")
    
    # sales = b0 + b1x1 + b2x2 + b3x3


    unit_sales = intercet + (beats[0]*modifyed_temp[0][0]) + (beats[1]*modifyed_temp[0][1]) + (beats[2]*modifyed_temp[0][2])

    unit_sales = str(unit_sales)

    
    lblshow.config(text = f"Unit Sales is : {unit_sales[ : 5]}")

    inp.delete(0, tk.END)

lbl = tk.Label(app, text = "Tempreture In Celcius", font = ("robort", 30, "bold"), foreground = "darkgreen", background = "lightgreen")
lbl.pack(pady = 20)

inp = tk.Entry(app, font = ("robort", 25), fg = "green")
inp.pack()

btn = tk.Button(app, text = "Check Sales", font = ("robort", 16, "bold"), background = "green", fg = "white", command = check_slaes)
btn.pack(pady = 20)

lblshow = tk.Label(app, text = "", font=("robort", 16, "italic"), fg = "green", background = "lightgreen")
lblshow.pack()

app.mainloop()