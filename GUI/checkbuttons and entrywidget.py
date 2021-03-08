from tkinter import *
root=Tk()
def getvalues():
    print("submitting form..")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("records.txt","w") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")
a=Label(root,text="welcome to tours and travels",font=("consolas",18,"italic"),pady=15).grid(row=0,column=4)
name=Label(root,text="Name:").grid(row=1,column=2)
phone=Label(root,text="Phone:").grid(row=2,column=2)
gender=Label(root,text="Gender:").grid(row=3,column=2)
paymentmode=Label(root,text="Payment mode:").grid(row=4,column=2)
foodservice=Label(root).grid(row=5,column=2)
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()#checkbox is a int var
e1=Entry(root,textvariable=namevalue).grid(row=1,column=3)
e2=Entry(root,textvariable=phonevalue).grid(row=2,column=3)
e3=Entry(root,textvariable=gendervalue).grid(row=3,column=3)
e4=Entry(root,textvariable=paymentmodevalue).grid(row=4,column=3)
e5=Checkbutton(root,text="want to pre-book your meals?",variable=foodservicevalue).grid(row=6,column=3)#checkbutton
#button n packing it and also assigning a command
bt1=Button(text="submit",command=getvalues).grid(row=7,column=3)
root.mainloop()