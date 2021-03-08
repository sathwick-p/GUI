from tkinter import *
root=Tk()
f1=Frame(root,background="black",borderwidth=9,relief=SUNKEN)
f1.pack(side="left",fill="y")
f2=Frame(root,borderwidth=9,background="black",relief=SUNKEN)
f2.pack(side="top",fill="x")
l2=Label(f2,text="welcome!",font=("Consolas",20,"bold"),foreground="blue")
l2.pack()
l1=Label(f1,text="helloworld")
l1.pack(padx=44,pady=44)
root.title("python-GUI")
root.mainloop()
#frame here acts as a div which is used in a website