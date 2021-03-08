from tkinter import *
root=Tk()
def hello():  #interaction
    print("wassup")
f1=Frame(root,borderwidth=9,background="blue",relief=SUNKEN,padx=30,pady=30)
f1.pack(side="left",anchor="nw")
x=Label(f1,text="hello",font=("consolas",15,"italic"))
x.pack(pady=20)
b1=Button(f1,text="submit",fg="green",command=hello)
b1.pack()
root.mainloop()