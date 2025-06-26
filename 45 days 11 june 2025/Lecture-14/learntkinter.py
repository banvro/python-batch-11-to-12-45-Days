# Tkinter
#     ----> Python GUI Library

# tkinter ---> design ---> Desktop applications

import tkinter as tk

app = tk.Tk()

app.geometry("900x350")
app.title("My First Tkinter App")
app.config(background = "#31eb1c")

# wedigts
# text ----> Label()
# input_box ----> Entery()
# buttons ---> Button() 

# font = (font_family, font_size, font_style)

lbl = tk.Label(app, text = "Hellow world", font = ("robort", 43, "bold"), fg = "#47f533", bg = "darkgreen")
lbl.pack(fill = "x", pady = 30, padx = 23, ipady = 5, side = "top")

inpx = tk.Entry(app, font = ("robort", 35, "italic"), bg = "#70f261")
inpx.pack()

btn = tk.Button(app, text = "Click Me", font = ("robort", 25, "bold"), fg = "#47f533", bg = "darkgreen")
btn.pack(pady = 30, ipadx = 40)

app.mainloop()



# methods to put wegigts

# 1) pack() -----> center
# 2) grid() ---> rows, columns
# 3) place() -----> pixcel





