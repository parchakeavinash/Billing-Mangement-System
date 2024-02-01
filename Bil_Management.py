from tkinter import *

window = Tk()
window.geometry("1000x500")
window.resizable(False, False)
window.title("Bill Management")


def Reset():
    entry_dosa.delete(0, END)
    entry_cookies.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_juice.delete(0, END)
    entry_pancakes.delete(0, END)
    entry_eggs.delete(0, END)
    entry_dosa.focus()


def Total():
    try:a1 = int(dosa.get())
    except:a1 = 0
    try:a2 = int(cookies.get())
    except:a2 = 0
    try:a3 = int(Tea.get())
    except:a3 = 0
    try:a4= int(coffee.get())
    except:a4 = 0
    try:a5 = int(juice.get())
    except:a5 = 0
    try:a6 = int(pancakes.get())
    except:a6 = 0
    try:a7 = int(eggs.get())
    except:a7 = 0

    # define cost of each items per quantity
    c1 = 50*a1
    c2 = 30*a2
    c3 = 12*a3
    c4 = 30*a4
    c5 = 30*a5
    c6 = 12*a6
    c7 = 6*a7

    lbl_total=Label(f2,font=("arial",20,"bold"), text="Total",width=16,fg="light yellow", bg="black")
    lbl_total.place(x=10,y = 50)

    entry_total = Entry(f2,font=("arial",20,"bold"),textvariable=Total_bill,bd=6,width=15, bg="light green")
    entry_total.place(x = 20,y = 100)

    total_cost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.", str("%.2f" %total_cost)
    Total_bill.set(string_bill)


Label(text="Bill Management", bg="black", fg="white", font=("calibri", 33), width="300", height=2).pack()

# Menu card
f = Frame(window, bg="light green", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=("calibri", 40, "bold"), fg="black", bg="light green").place(x=80, y=0)

Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Dosa........Rs.50/plate").place(x=10, y=80)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Cookies........Rs.30/plate").place(x=10, y=110)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Tea........Rs.12/cup").place(x=10, y=140)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Coffee........Rs.30/cup").place(x=10, y=170)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Juice........Rs.30/glass").place(x=10, y=200)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Pancakes........Rs.12/pack").place(x=10, y=230)
Label(f, font=("Arial", 15, 'bold'), bg="light green", fg="black", text="Eggs........Rs.6/egg").place(x=10, y=260)

# Bill
f2 = Frame(window, bg="light yellow", highlightbackground="black", highlightthickness=1, width=300,
           height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="Bill",font=("calibri",20), bg="light yellow")
Bill.place(x=120, y=10)


# Entry work
f1 = Frame(window, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

dosa = StringVar()
cookies = StringVar()
Tea = StringVar()
coffee = StringVar()
juice = StringVar()
pancakes = StringVar()
eggs = StringVar()
Total_bill = StringVar()

# label
lbl_dosa = Label(f1, font=("aria", 20, "bold"), text="Dosa", width=12, fg="blue4")
lbl_cookies = Label(f1, font=("aria", 20, "bold"), text="Cookies", width=12, fg="blue4")
lbl_tea = Label(f1, font=("aria", 20, "bold"), text="Tea", width=12, fg="blue4")
lbl_coffee = Label(f1, font=("aria", 20, "bold"), text="Coffee", width=12, fg="blue4")
lbl_juice = Label(f1, font=("aria", 20, "bold"), text="Juice", width=12, fg="blue4")
lbl_pancakes = Label(f1, font=("aria", 20, "bold"), text="Pancakes", width=12, fg="blue4")
lbl_eggs = Label(f1, font=("aria", 20, "bold"), text="Eggs", width=12, fg="blue4")
lbl_dosa.grid(row=1, column=0)
lbl_cookies.grid(row=2, column=0)
lbl_tea.grid(row=3, column=0)
lbl_coffee.grid(row=4, column=0)
lbl_juice.grid(row=5, column=0)
lbl_pancakes.grid(row=6, column=0)
lbl_eggs.grid(row=7, column=0)

# entry
entry_dosa = Entry(f1, font=("aria", 20, "bold"), textvariable=dosa, bd=6, width=8, bg='light pink')
entry_dosa.grid(row=1, column=1)
entry_cookies = Entry(f1, font=("aria", 20, "bold"), textvariable=cookies, bd=6, width=8, bg='light pink')
entry_cookies.grid(row=2, column=1)
entry_tea = Entry(f1, font=("aria", 20, "bold"), textvariable=Tea, bd=6, width=8, bg='light pink')
entry_tea.grid(row=3, column=1)
entry_coffee = Entry(f1, font=("aria", 20, "bold"), textvariable=coffee, bd=6, width=8, bg='light pink')
entry_coffee.grid(row=4, column=1)
entry_juice = Entry(f1, font=("aria", 20, "bold"), textvariable=juice, bd=6, width=8, bg='light pink')
entry_juice.grid(row=5, column=1)
entry_pancakes = Entry(f1, font=("aria", 20, "bold"), textvariable=pancakes, bd=6, width=8, bg='light pink')
entry_pancakes.grid(row=6, column=1)
entry_eggs = Entry(f1, font=("aria", 20, "bold"), textvariable=eggs, bd=6, width=8, bg='light pink')
entry_eggs.grid(row=7, column=1)

# buttons
btn_reset = Button(f1, bd=5, fg="black", bg="light blue", font=("ariel", 16, "bold"), width=10, text="Reset",
                   command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="light blue", font=("ariel", 16, "bold"), width=10, text="Total",
                   command=Total)
btn_total.grid(row=8, column=1)

window.mainloop()
