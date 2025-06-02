import tkinter as tk 
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost", port = 3307, username = "root", password = "1234",
    database = "morning1050"
)

cursr = conn.cursor()


def getingdata():
    name = ent1.get()
    email = ent2.get()
    phon = ent3.get()
    msg = ent4.get('1.0', tk.END)

    cursr.execute(f"insert into newcontactus values('{name}', '{email}', '{phon}', '{msg}')")

    conn.commit()

    lbl9.config(text = "Data Saved!!!!")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete('1.0',tk.END)



app = tk.Tk()
app.geometry("800x500")
app.title("Contact Us form")
app.config(background = "#3af51d")


lblx = tk.Label(app, text = " ")
lbl1 = tk.Label(app, text = "Name", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl2 = tk.Label(app, text = "Email", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl3 = tk.Label(app, text = "Number", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl4 = tk.Label(app, text = "Message", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")

lbl5 = tk.Label(app, text = ":", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl6 = tk.Label(app, text = ":", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl7 = tk.Label(app, text = ":", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")
lbl8 = tk.Label(app, text = ":", font = ("robort", 28, "bold"), bg = "#3af51d", fg = "darkgreen")

lbl9 = tk.Label(app, text = "", font = ("robort", 15, "italic"), bg = "#3af51d", fg = "darkgreen")

ent1 = tk.Entry(app, font = ("robort", 24, "italic"), bg = "#9df78f", fg = "red")
ent2 = tk.Entry(app, font = ("robort", 24, "italic"), bg = "#9df78f", fg = "red")
ent3 = tk.Entry(app, font = ("robort", 24, "italic"), bg = "#9df78f", fg = "red")
ent4 = tk.Text(app, font = ("robort", 24, "italic"), bg = "#9df78f", fg = "red", width = 20, height = 3)


btn = tk.Button(app, text = "Send Message", font = ("robort", 20, "bold"), bg = "#1b7c0c", fg = "lightgreen", command = getingdata)
btn.grid(row = 5, column = 3, pady = 20)

lblx.grid(row = 0, column = 0, padx = 50, pady = 30)

lbl1.grid(row = 1, column = 1)
lbl2.grid(row = 2, column = 1, pady = 10)
lbl3.grid(row = 3, column = 1)
lbl4.grid(row = 4, column = 1, pady = 10)

lbl5.grid(row = 1, column = 2, padx = 8)
lbl6.grid(row = 2, column = 2)
lbl7.grid(row = 3, column = 2)
lbl8.grid(row = 4, column = 2)
lbl9.grid(row = 6, column = 3)

ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3)
ent3.grid(row = 3, column = 3)
ent4.grid(row = 4, column = 3)

app.mainloop()