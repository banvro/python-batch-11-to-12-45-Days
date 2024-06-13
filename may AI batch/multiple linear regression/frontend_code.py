import tkinter as tk
import joblib

model = joblib.load("extractfeatures_prediction.joblib")


print(model.coef_)

print(model.intercept_)



# app = tk.Tk()
# app.geometry("500x400")
# app.title("Multiple LInear Regression")
# app.config(background = "lightgreen")




# app.mainloop()