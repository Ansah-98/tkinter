"""
binding is used to attach specific event handlers to events 
its more of a custom command parameter in the button and check button

unbinding events removes the specified event handler from the event
"""

from tkinter import BooleanVar, Checkbutton, Tk, BOTH, Text, LEFT,RIGHT, messagebox,S

from tkinter.ttk import Frame ,Label,Button

class  Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent 
        self.initUi()

    def initUi(self):
        self.parent.title("commands")
        self.pack(fill= BOTH, expand = True)

        self.parent.bind("<Escape>" , self.quitApp)
        btn = Button(self,text="Click")
        btn.pack(side = LEFT)

        self.var  = BooleanVar()
        cb = Checkbutton(self , text = "Bind event" , variable = self.var , command = lambda: self.onBind(btn))
        cb.pack(side=RIGHT, anchor= S)

    def onBind(self,w):

        if self.var.get() == True :
            w.bind("<Button-1>" , self.onclick )
        else:
            w.unbind("<Button-1>")

    def onclick(self, e):
        print("clicked")

    def quitApp(self,e):
        ret = messagebox.askquestion( "Question are you sure you want to quit ", default  =messagebox.NO)
        if ret == "yes":
            self.quit()


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == "__main__":
    main()