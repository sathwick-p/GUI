from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
canvaswidget=Canvas(root,width=canvas_width,height=canvas_height).pack()
#the line goes from x1,x2 to y1,y2
Canvas.create_line(0,30,800,30)
root.mainloop()