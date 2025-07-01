import tkinter as tk 
import mysql.connector

connn = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    username = "root",
    password = "1234",
    database = "morning11"
)

cuserr = connn.cursor()

def savedata():
    a = ent1.get()
    b = ent2.get()
    c = ent3.get()
    d = ent4.get()
    e = ent5.get("1.0", tk.END)

    cuserr.execute(f"insert into contact_us(full_name, age, phone_number, email, message) values('{a}', {b}, '{c}','{d}', '{e}');")

    connn.commit()

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete(0, tk.END)
    ent5.delete("1.0", tk.END)




app = tk.Tk()
app.geometry("730x600")

x = tk.Label(app, text = "")

lbl1 = tk.Label(app, text = "Full Name", font = ("robort", 23, "bold"))
lbl2 = tk.Label(app, text = "Age", font = ("robort", 23, "bold"))
lbl3 = tk.Label(app, text = "Phone No.", font = ("robort", 23, "bold"))
lbl4 = tk.Label(app, text = "E-Mail", font = ("robort", 23, "bold"))
lbl5 = tk.Label(app, text = "Message", font = ("robort", 23, "bold"))

lbl6 = tk.Label(app, text = ":", font = ("robort", 23, "bold"))
lbl7 = tk.Label(app, text = ":", font = ("robort", 23, "bold"))
lbl8 = tk.Label(app, text = ":", font = ("robort", 23, "bold"))
lbl9 = tk.Label(app, text = ":", font = ("robort", 23, "bold"))
lbl10 = tk.Label(app, text = ":", font = ("robort", 23, "bold"))

ent1 = tk.Entry(app, font = ("robort", 23))
ent2 = tk.Entry(app, font = ("robort", 23))
ent3 = tk.Entry(app, font = ("robort", 23))
ent4 = tk.Entry(app, font = ("robort", 23))
ent5 = tk.Text(app, font = ("robort", 23), height = 4, width = 20)


x.grid(row = 0, column = 0,padx = 40, pady = 30)
lbl1.grid(row = 1, column = 1)
lbl2.grid(row = 2, column = 1, pady = 20)
lbl3.grid(row = 3, column = 1)
lbl4.grid(row = 4, column = 1, pady = 20)
lbl5.grid(row = 5, column = 1)

lbl6.grid(row = 1, column = 2, padx = 10)
lbl7.grid(row = 2, column = 2)
lbl8.grid(row = 3, column = 2)
lbl9.grid(row = 4, column = 2)
lbl10.grid(row = 5, column = 2)

ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3)
ent3.grid(row = 3, column = 3)
ent4.grid(row = 4, column = 3)
ent5.grid(row = 5, column = 3)

btn = tk.Button(app, text = "Submit", font = ("robort", 20, "bold"), command = savedata)
btn.grid(row = 6, column = 3, pady = 20)

app.mainloop()