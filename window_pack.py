"""
the following example creates the windows layout using pack manager 

"""
from tkinter import Tk,BOTH,LEFT,RIGHT,X,Y,Text,TOP,S
from tkinter.ttk import Label,Style,Button,Frame


class Window(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.parent.title("window")
        self.pack(fill=BOTH,expand=True)

        frame = Frame(self)
        frame.pack(fill = X)

        lbl =Label(frame, text="window")
        lbl.pack(side=LEFT, padx=5, pady=5)

        frame1 = Frame(self)
        frame1.pack(fill=BOTH , expand= True)

        txt = Text(frame1,width=20,height=10)
        txt.pack(side = LEFT ,fill=BOTH ,expand=True , padx= 5)

        frame2 = Frame(frame1)
        frame2.pack(side= LEFT, fill=Y )
        actBtn = Button(frame2, text="activate")
        actBtn.pack(side = TOP, fill= Y )

        frame3  = Frame(self )
        frame3.pack(fill= X, )

        hlpBtn = Button(frame3 , text="help")
        hlpBtn.pack(side = LEFT , pady=5 , padx=5)

        okBtn = Button(frame3 , text= "ok" )
        okBtn.pack(side=RIGHT,padx=5)
def main():
    root =Tk()
    root.geometry("300x300+300+300")
    app = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()