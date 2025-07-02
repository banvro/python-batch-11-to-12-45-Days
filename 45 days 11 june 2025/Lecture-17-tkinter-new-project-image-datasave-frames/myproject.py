import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(
    host = "localhost",
    username = "root",
    port = 3307,
    password = "1234",
    database = "morning11"
)

cr = conn.cursor()


def savinginfo():
    full_nm = ent1.get()
    emal = ent2.get()
    phon = ent3.get()
    msg = ent4.get("1.0", tk.END)

    cr.execute(f"insert into contactinfo(full_name, email_address, phone_number, message) values('{full_nm}', '{emal}', '{phon}', '{msg}');")
    
    conn.commit()

    messagebox.showinfo("Data Saved", "Your Message saveed sucessfuly in Database..")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete("1.0", tk.END)

    showinfo.config(text = f"Thank you! {full_nm} ! Will connetct shortly")




app = tk.Tk()
app.geometry("1100x680")
app.title("My Contact Us Form")
app.config(background = "#68f522")


frame1 = tk.Frame(app, relief = "raised", borderwidth = 20, bg = "#33850b")
frame1.pack(fill = "x")

contact_lbl = tk.Label(frame1, text = "Contact Us Now", font = ("robort", 38, "bold"), bg = "#33850b", fg = "#68f522")
contact_lbl.pack()



frame2 = tk.Frame(app, relief = "groove", borderwidth = 20, background = "darkgreen")
frame2.pack(fill = "x")

img = Image.open("banner.jpg")
new_img = ImageTk.PhotoImage(img)

imgg = tk.Label(frame2, image = new_img, height = 200)
imgg.pack()

frame3 = tk.Frame(app, relief = "sunken", borderwidth = 20)
frame3.pack(fill = "x")

frame4 = tk.Frame(frame3)
frame4.grid(row = 0, column = 0)

frame5 = tk.Frame(frame3)
frame5.grid(row = 0, column = 1)

lbl0 = tk.Label(frame4, text = "")

lbl1 = tk.Label(frame4, text = "Full Name", font = ("robort", 20, "bold"))
lbl2 = tk.Label(frame4, text = "Email-Add.", font = ("robort", 20, "bold"))

lbl3 = tk.Label(frame5, text = "Phone No.", font = ("robort", 20, "bold"))
lbl4 = tk.Label(frame5, text = "Message", font = ("robort", 20, "bold"))

lbl5 = tk.Label(frame4, text = ":", font = ("robort", 20, "bold"))
lbl6 = tk.Label(frame4, text = ":", font = ("robort", 20, "bold"))

lblx = tk.Label(frame5, text = "")
lbl7 = tk.Label(frame5, text = ":", font = ("robort", 20, "bold"))
lbl8 = tk.Label(frame5, text = ":", font = ("robort", 20, "bold"))

ent1 = tk.Entry(frame4, font = ("robort", 20))
ent2 = tk.Entry(frame4, font = ("robort", 20))

ent3 = tk.Entry(frame5, font = ("robort", 20))
ent4 = tk.Text(frame5, font = ("robort", 20), height = 2, width = 20)


lbl0.grid(row = 0, column = 0, padx = 10, pady = 5)
lbl3.grid(row = 1, column = 1)
lbl4.grid(row = 2, column = 1)
lbl7.grid(row = 1, column = 2)
lbl8.grid(row = 2, column = 2)
ent3.grid(row = 1, column = 3)
ent4.grid(row = 2, column = 3, pady = 18)

lblx.grid(row = 0, column = 0, padx = 20, pady = 5)
lbl1.grid(row = 1, column = 1)
lbl2.grid(row = 2, column = 1, pady = 18)
lbl5.grid(row = 1, column = 2)
lbl6.grid(row = 2, column = 2)
ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3)


frame6 = tk.Frame(app)
frame6.pack(fill = "x")

btn = tk.Button(frame6, text = "Send Message", font = ("robort", 18, "bold"), bg = "#33850b", fg = "#68f522", command = savinginfo)
btn.pack()

showinfo = tk.Label(frame6, text = "", font = ("robort", 18, "bold"), bg = "#68f522", fg = "#184700")
showinfo.pack(pady = 20, fill = "x") 




app.mainloop()