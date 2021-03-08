from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("GRAPHICAL USER INTERFACE")
#Attributes of Label: The Label widget is a standard Tkinter widget used to display a text or image on the screen.  There are a lot of attributes of Label widget. Some important attributes are discussed below:
# bg: The normal background color displayed behind the label and indicator.
# fg: This option specifies the color of the text (foreground color). If you are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.
# padx: Extra space added to the left and right of the text within the widget. Default is 1.
# pady: Extra space added above and below the text within the widget. Default is 1.
# relief: Specifies the appearance of a decorative border around the label. There are five types of reliefs, such that FLAT, RAISED, SUNKEN, GROOVE, RIDGE. The default is FLAT.
# font: If you are displaying text in this label (with the text or textvariable option), the font option specifies the style, size and other characteristics (i.e. bold, italic etc.) of the font and in this style the text will be displayed.
# text: To display one or more lines of text in a label widget, set this option to a string containing the text. Internal newlines (“\n”) will force a line break.
# justify: Specifies how multiple lines of text will be aligned with respect to each other: LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.
# height: The vertical dimension of the new frame.
# width: The horizontal dimension of the new frame. If this option is not set, the label will be sized to fit its contents.
title_label=Label(text="WELCOME TO GUI",background="black",foreground="white",padx=23,pady=23,font=("consolas",35,"bold"),borderwidth=3,relief=RIDGE) 
title_label.pack(anchor="ne",side="bottom",fill=Y,padx=30,pady=30)
#important pack options
#anchor:nw,ne,sw,se etc. these are the directions of a compass like ne stands for northeast and it moves the whole lable to ne of the page
#side: top,left,right,bottom
#fill: Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically)
#padx:giving padding wrt to the window 
#pady:
root.mainloop()