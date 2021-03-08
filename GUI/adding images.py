from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("600x600")
# pic=PhotoImage(file="download.jpg")
# x=Label(image=pic)
# x.pack()
# for jpg images image .open the above is for png images only
image=Image.open("download.jpg")
photo=ImageTk.PhotoImage(image)
x=Label(image=photo)
x.pack()
root.mainloop()
