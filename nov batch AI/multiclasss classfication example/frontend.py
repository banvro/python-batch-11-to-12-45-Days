import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib

xyz = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"] 

model = joblib.load("Image_classification.joblib")

def classify_image(img_path):
    read_img = Image.open(img_path)
    gray_img = read_img.convert("L").resize((28, 28))
    array_image = np.array(gray_img)

    new_img = array_image.flatten()
    reshped_image = new_img.reshape(1, -1)
    output = model.predict(reshped_image)
    return output

def uploadingImage():
    image_path = filedialog.askopenfilename()
    img_read = Image.open(image_path)
    img_read.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img_read)
    imshoww.config(image = img)
    imshoww.image = img

    output = classify_image(image_path)

    lbloutput.config(text = f"Your upload Image is : {xyz[output[0]]}.")

app = tk.Tk()
app.geometry("600x600")
app.title("Fashion Image Classification")
app.config(background="#84fae6")

lbl = tk.Label(app, text = "Image Classification", font = ("robort", 27, "bold"), bg = "#03856f", fg = "white")
lbl.pack(fill = "x", ipady = 6)

imshoww = tk.Label()
imshoww.pack()

butn = tk.Button(app, text = "Upload Image", font = ("robort", 19, "bold"), bg = "#03856f", fg = "white", command = uploadingImage)
butn.pack()

lbloutput = tk.Label(app, text = "", background = "#84fae6", font=("robort", 18,))
lbloutput.pack(pady = 6)

app.mainloop()