"""
creating rows of buttons wi  pack manager 
"""

from tkinter import Tk, BOTH,LEFT
from tkinter.ttk import Frame , Button

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent  = parent
        self.initUi()

    def initUi(self):
        self.parent.title("rows of button")
        self.pack(fill=BOTH,expand=True)
        frame = Frame(self) 
        frame.pack(padx=5,pady= 5)

        frame2 = Frame(self)
        frame2.pack()

        button1 = Button(frame, text="Button")
        button1.pack(side=LEFT , padx = 5)
        button2 = Button(frame, text="Button")
        button2.pack(side=LEFT)

        button3 = Button(frame, text="BUTTON")
        button3.pack(side=LEFT,padx= 5)

        button4 = Button(frame , text= "Button")
        button4.pack(side = LEFT)

        btn1 = Button(frame2,text="Button")
        btn1.pack(side = LEFT,padx= 5)
        btn2 = Button(frame2 , text="Button")
        btn2.pack(side= LEFT)
        btn3 = Button(frame2 , text="Button")
        btn3.pack(side = LEFT , padx=5)
        btn4 = Button(frame2 ,text="Button")
        btn4.pack(side=LEFT)

def main():
    root = Tk()
    root.geometry = ("300x200+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()