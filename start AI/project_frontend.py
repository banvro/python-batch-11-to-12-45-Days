import tkinter as tk
import joblib
import numpy as np
import pandas as pd

my_model = joblib.load("heart_decisis_prediction.joblib")

def checking_heart_decieas():
    a1 = en1.get()
    a2 = en2.get()
    a3 = en3.get()
    a4 = en4.get()
    a5 = en5.get()
    a6 = en6.get()
    a7 = en7.get()
    a8 = en8.get()
    a9 = en9.get()
    a10 = en10.get()
    a11 = en11.get()
    
    user_detail = (int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(a8), int(a9), int(a10), int(a11))

    arr = np.array(user_detail)

    user_d = arr.reshape(1, -1)

    zx =my_model.predict(user_d)
    print(type(zx))

    if zx[0] == 0:
        lbl3.config(text="You have not any heart problem, you are fit")
    
    else:
        lbl3.config(text="you are with heart deceis.")

    print(zx, "xxxxxxxxxxx")

window =tk.Tk()

window.geometry("500x800")
window.title("Heart Decies Checkup")

f1 = tk.Frame(window, relief="groove", borderwidth=5)
f1.pack()


lbl = tk.Label(f1, text="Enter User Madical Details ")
lbl.pack()


f2 = tk.Frame(window, relief="groove", borderwidth=5)
f2.pack()

en1 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en1.pack()

en2 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en2.pack()

en3 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en3.pack()

en4 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en4.pack()

en5 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en5.pack()

en6 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en6.pack()

en7 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en7.pack()

en8 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en8.pack()

en9 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en9.pack()

en10 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en10.pack()

en11 = tk.Entry(f2, relief="solid", font=("robort", 20, "italic"))
en11.pack()


btn = tk.Button(f2, text = "Check Heart Decieas", font=("robort", 15, "bold"), command=checking_heart_decieas)
btn.pack()


f3 = tk.Frame(window, relief="ridge", borderwidth=5)
f3.pack()

lbl3 = tk.Label(f3, text = "", font=("robort", 15, "bold"), fg = "Red")
lbl3.pack()


window.mainloop()






