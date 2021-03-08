from tkinter import *
root=Tk()
#gridlayout 
def getvalues():
    print(uservalue.get())   #.get()function returns the value given in the uservalue string
    print(passwordvalue.get())
a=Label(root,text="Username:")
b=Label(root,text="Password:")
a.grid()  #same function as the pack() function
b.grid(row=1)
# variable classes in tkinter
# BooleanVar,DoubleVar,StringVar,IntVar
uservalue=StringVar()
passwordvalue=StringVar()
userentery=Entry(root,textvariable=uservalue)  #Entry is used to create a textbox widget to enter values in it
passwordentery=Entry(root,textvariable=passwordvalue)
userentery.grid(row=0,column=1)
passwordentery.grid(row=1,column=1)
bt1=Button(root,text="submit",command=getvalues)
bt1.grid()
root.mainloop()