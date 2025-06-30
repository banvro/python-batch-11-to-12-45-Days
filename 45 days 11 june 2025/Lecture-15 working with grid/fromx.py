import tkinter as tk

main = tk.Tk()
main.geometry("900x700")
main.title("Contact Us Form")

x = tk.Label(main, text = "")
x.grid(row = 0, column = 0, padx = 60, pady = 30)

full_name = tk.Label(main, text = "Full Name", font = ("robort", 25, "bold"))
full_name.grid(row = 1, column = 1)


xyz = tk.Entry(main, font = ("robort", 25, "bold"))
xyz.grid(row = 1, column = 2)

main.mainloop()