import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x500")

# frames 
img = "myimage.jpg"
x = Image.open(img)
new_img = ImageTk.PhotoImage(x)

lbl = tk.Label(window, image = new_img, height=160, width=160)
lbl.pack()

fram1 = tk.Frame(window, relief = "groove", borderwidth=20)
fram1.pack()

fram2 = tk.Frame(window, relief = "sunken", borderwidth=20)
fram2.pack()

lbl = tk.Label(fram1, text="hwlloe", font = ("robort", 20, "bold"))
lbl.pack()

lbl1 = tk.Label(fram2, text="hwlloe", font = ("robort", 20, "bold"))
lbl1.grid(row=0, column=0)

entr = tk.Entry(fram2, font = ("robort", 20, "bold"))
entr.grid(row=0, column=1)



window.mainloop()
