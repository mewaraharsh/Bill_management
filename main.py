from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Bill Mangement")
root.resizable(False,False)
def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancake.delete(0,END)
    entry_eggs.delete(0,END)
    entry_poha.delete(0,END)
    entry_Maggie.delete(0,END)
def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(Tea.get())
    except: a3=0

    try:a4=int(coffee.get())
    except: a4=0

    try:a5=int(juice.get())
    except: a5=0

    try:a6=int(pancakes.get())
    except: a6=0

    try:a7=int(eggs.get())
    except: a7=0

    try:a8=int(Poha.get())
    except: a8=0

    try:a9=int(Maggie.get())
    except: a9=0

    """Define cost of each item"""
    c1 = 60*a1
    c2 = 30*a2
    c3 = 10*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 20*a6
    c7 = 10*a7
    c8 = 20*a8
    c9 = 40*a9

    lbl_Total = Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black").place(x=700,y=160)
    entry_total = Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen").place(x=720,y=200)
    totalcost = c1+c2+c3+c4+c5+c6+c7+c8+c9
    string_bill = "₹",str('%.2f'%totalcost)
    Total_bill.set(string_bill)


Label(text="BILL MANAGEMENT", bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()
"""Menu Card"""
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=470)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Dosa........₹60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Cookies.....₹30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Tea.........₹10/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Coffee......₹100/cup",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Juice.......₹20/glass",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Pancakes....₹20/pack",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Eggs........₹10/egg",fg="black",bg="lightgreen").place(x=10,y=260)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Poha........₹20/plate",fg="black",bg="lightgreen").place(x=10,y=290)
Label(f,font=("Lucida Calligrapghy",15,'bold'),text="Maggie......₹40/plate",fg="black",bg="lightgreen").place(x=10,y=320)

"""Entry Work"""
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()
dosa = StringVar()
cookies = StringVar()
Tea = StringVar()
coffee = StringVar()
juice = StringVar()
pancakes = StringVar()
eggs = StringVar()
Poha = StringVar()
Maggie= StringVar()
Total_bill=StringVar()

"""Label"""
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
lbl_Coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue4")
lbl_juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")
lbl_Pancakes=Label(f1,font=("aria",20,'bold'),text="Pancakes",width=12,fg="blue4")
lbl_eggs=Label(f1,font=("aria",20,'bold'),text="Eggs",width=12,fg="blue4")
lbl_poha=Label(f1,font=("aria",20,'bold'),text="Poha",width=12,fg="blue4")
lbl_Maggie=Label(f1,font=("aria",20,'bold'),text="Maggie",width=12,fg="blue4")
lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_Pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)
lbl_poha.grid(row=8,column=0)
lbl_Maggie.grid(row=9,column=0)

"""Entry"""
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",20,'bold'),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_Coffee=Entry(f1,font=("aria",20,'bold'),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_juice=Entry(f1,font=("aria",20,'bold'),textvariable=juice,bd=6,width=8,bg="lightpink")
entry_pancake=Entry(f1,font=("aria",20,'bold'),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_eggs=Entry(f1,font=("aria",20,'bold'),textvariable=eggs,bd=6,width=8,bg="lightpink")
entry_poha=Entry(f1,font=("aria",20,'bold'),textvariable=Poha,bd=6,width=8,bg="lightpink")
entry_Maggie=Entry(f1,font=("aria",20,'bold'),textvariable=Maggie,bd=6,width=8,bg="lightpink")

entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Coffee.grid(row=4,column=1)
entry_juice.grid(row=5,column=1)
entry_pancake.grid(row=6,column=1)
entry_eggs.grid(row=7,column=1)
entry_poha.grid(row=8,column=1)
entry_Maggie.grid(row=9,column=1)

"""Buttons"""
btn_reset=Button(f1,bd=5,fg="blue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=10,column=0)
btn_Total=Button(f1,bd=5,fg="blue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_Total.grid(row=10,column=1)

"""Bill"""
f2 = Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=470).place(x=690,y=118)
Bill = Label(f2,text="Bill",font=('calibri',20),bg="lightyellow").place(x=820,y=120)

root.mainloop()