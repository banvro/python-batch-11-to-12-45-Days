import tkinter as tk
import joblib
import numpy as np

# pip install joblib
# pip install numpy

model = joblib.load("predicted_sallery_by_expreience.joblib")


def check_sallery():
    exp = int(ent.get())

    xyz = np.array(exp)

    exp_reshape = xyz.reshape(1, -1)
    
    result = model.predict(exp_reshape)
    real_resilt = result[0]

    lblhow.config(text = f"Based On Experience i.e {exp}, Your Predicted Sallery is : {real_resilt}")

app = tk.Tk()
app.geometry("700x300")
app.title("Predict Sallery")
app.config(bg = "light green")



lbl = tk.Label(app, text = "Enter Your Experience", font = ("robprt", 27, "bold"), background="light green", foreground = "dark green")
lbl.pack(pady = 16)

ent = tk.Entry(app, font = ("robprt", 22))
ent.pack()

btn = tk.Button(app, text = "Check Sallery", font = ("robprt", 20, "bold"), fg = "light green", bg = "dark green", command = check_sallery)
btn.pack(pady = 16)


lblhow = tk.Label(app, text = "", fg = "dark green", bg = "light green", font = ("robprt", 16))
lblhow.pack()

app.mainloop()





