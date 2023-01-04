"""
creating a new folder screen using the pack manager in tkinter

"""
from tkinter import Tk,BOTH,LEFT,RIGHT,X,Text
from tkinter.ttk import Frame,Button,Label,Entry

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent 
        self.initUi()
    
    def initUi(self):
        self.parent.title("new folder ")
        self.pack(fill = BOTH , expand  = True )

        frame1  = Frame(self)
        frame1.pack(fill=X)
        
        lbl1 = Label(frame1 ,text="Name")
        lbl1.pack(side=LEFT ,padx=5, pady=5)

        ent = Entry(frame1)
        ent.pack(side=LEFT , fill=X ,expand= True )

        frame2 = Frame(self )
        frame2.pack(fill=BOTH, expand = True)
        txt = Text(frame2,width=20,height=10 )
        txt.pack(fill=BOTH, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        closeBtn = Button(frame3 , text="close")
        closeBtn.pack(side=RIGHT ,pady=5 )
        OkBtn = Button(frame3,text="Ok")
        OkBtn.pack(side=RIGHT,padx=5)


def main():
    root = Tk()
    root.geometry("300x500+250+100")
    app = Example(root)
    root.mainloop()

if __name__=="__main__":
    main()    