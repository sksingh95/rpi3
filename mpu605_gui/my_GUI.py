from tkinter import *

class GUI:
    def __init__(self):
        """ Initialize the x, y, z and heading property """
        self.x = StringVar()
        self.x.set("x")
        self.y = StringVar()
        self.y.set("y")
        self.z = StringVar()
        self.z.set("z")
        self.label_text = StringVar()
        self.label_text.set("Heading")

    def createGUI(self, rootWin):
        """ Create GUI and return a frame object """
        self.rootWin = rootWin
        self.frame = Frame(rootWin)
        self.lbl_heading = Label(self.frame, text="Heading", textvariable=self.label_text)
        self.lbl_heading.pack()
        self.lbl_x = Label(self.frame, text="x", textvariable=self.x)
        self.lbl_x.pack()
        self.lbl_y = Label(self.frame, text="y", textvariable=self.y)
        self.lbl_y.pack()
        self.lbl_z = Label(self.frame, text="z", textvariable=self.z)
        self.lbl_z.pack()
        return self.frame

    def setxyz(self,x,y,z):
        """ Update the value of x, y, z """
        self.x.set(x)
        self.y.set(y)
        self.z.set(z)

    def setColHeading(self, heading):
        """ Update column headng """
        self.label_text.set(heading)

    def changeFgColor(self, color):
        """ Change the color of forground text """
        self.lbl_x.config(fg=color)
        self.lbl_y.config(fg=color)
        self.lbl_z.config(fg=color)
