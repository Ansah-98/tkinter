from tkinter import Checkbutton, Tk , BOTH,Text,Button,LEFT,RIGHT,S
from tkinter.ttk import Frame,Label

class Example(Frame):
    def  __init__(self,parent):
        Frame.__init__(self,parent, name = "frame")
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.parent.title("Event window")
        self.pack(fill = BOTH, expand = True) 

        btn = Button(self, text="button" , command = self.onButton1click)
        btn.pack(side = LEFT, padx = 15)

        cBtn = Checkbutton(self, text = "checkButton", command = self.onbutton2click)
        cBtn.pack(side = LEFT,anchor=S)

    def onbutton2click(self):
        print("check button has been clicked") 
    
    def onButton1click(self):
        print("push button has been clicked")


class main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()