import tkinter as tk
# pip install pillow
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("600x500")

img = Image.open("myimg.jpg")
new_img = ImageTk.PhotoImage(img)

lbl = tk.Label(app, image = new_img, width = 600)
lbl.pack()
    

app.mainloop()
