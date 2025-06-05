import tkinter as tk 

app = tk.Tk()
app.geometry("800x500")
app.config(background = "#4cfc2d")

frame1 = tk.Frame(app, relief = "raised", borderwidth = 20, background = "#12fccd")
frame1.pack(fill = "x")

frame2 = tk.Frame(app, relief = "groove", borderwidth = 20, background = "#f807b8")
frame2.pack(fill = "x")

lbl = tk.Label(frame1, text = "Contact Us", font = ("robort", 35, "bold"),  background = "#12fccd")
lbl.pack(pady = 20)

xy = tk.Label(frame2, text = "Name", font = ("robort", 28, "bold"),  background = "#f807b8")
xy.grid(row = 0, column = 0)




app.mainloop()