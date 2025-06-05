import tkinter as tk 
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("800x500")
app.config(background = "#4cfc2d")

frame1 = tk.Frame(app, relief = "raised", borderwidth = 20, background = "#12fccd")
frame1.pack(fill = "x")

myimg = Image.open("nature.jpg")
imgg = ImageTk.PhotoImage(myimg)

imgx = tk.Label(frame1, image = imgg, width = 20)
imgx.pack()

app.mainloop()




# Last ---> tkinter
#     Message, screens distory