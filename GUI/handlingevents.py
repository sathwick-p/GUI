from tkinter import *
root=Tk()
def yup(event): #event is the argument passed by tkinter 
    print(f"You clicked the button at {event.x},{event.y}")
root.title("Handling events in GUI")
widget=Button(root,text="Click me please").pack()
widget.bind('<Button-1>',yup)  #mouse button is pressed over the widget
root.mainloop()