"""
making corner buttons with the pack layout manager

"""

from tkinter import Tk , BOTH, LEFT,RIGHT,S
from tkinter.ttk import Frame,Button

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent 
        self.initUi()
    
    def initUi(self):
        self.parent.title("corner buttons")
        self.pack(fill =BOTH, expand = True)


        button1 = Button(self , text= "close")
        button1.pack(side=RIGHT , anchor= S)

        button2 = Button(self,text= "OK")
        button2.pack(anchor=S, padx=5 ,side=RIGHT)

def main():
    root = Tk()
    root.geometry("300x300+300+250")
    app  = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()