"""
designing ui for calculator  using the grid layout manager 

"""
from tkinter import  Entry, Tk, BOTH,X,Y,LEFT,RIGHT,TOP, S,Text,W,E
from tkinter.ttk import Frame,Label, Button,Style
class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.parent.title("calculator")
        self.pack(fill= BOTH, expand=True)

        Style().configure('TButton' , padding =( 0, 5,0,5 ) )
        font = ('serif:10')


        self.columnconfigure(0,pad =3 )
        self.columnconfigure(1,pad =3)
        self.columnconfigure(2,pad=3)
        self.columnconfigure(3,pad=3 )

        self.rowconfigure(0,pad=3)
        self.rowconfigure(1,pad=3)
        self.rowconfigure(2,pad=3)
        self.rowconfigure(3,pad=3)
        

        entry = Entry(self)
        entry.grid(row =0, column=0, columnspan=4, sticky=W+E)
        cls = Button(self,text= "cls")
        cls.grid(row=1,column= 0)
        bck = Button(self, text= "Back")
        bck.grid(row=1,column=1)
        lbl = Button(self)
        lbl.grid(row =1, column=2)
        clo = Button(self,text="close")
        clo.grid(row=1,column=3)
        sev = Button(self, text=7)
        sev.grid(row =2 ,column= 0)
        eig = Button(self, text = "8")
        eig.grid(row=2 ,column=1)
        nin = Button(self , text= "9")
        nin.grid(row=2,column=2)
        div = Button(self,text ="/")
        div.grid(row= 2 ,column=3)
        four = Button(self,text="4")
        four.grid(row=3,column=0)
        five = Button(self,text="5")
        five.grid(row =3, column=1)
        six = Button(self,text="6")
        six.grid(row =3,column=2)
        mul = Button(self,text="x")
        mul.grid(row =3,column=3)
        one = Button(self,text="1")
        one.grid(row =4 , column=0)
        two = Button(self,text="2")
        two.grid(row=4, column=1)
        three = Button(self,text="3")
        three.grid(row=4 ,column=2)
        mins = Button(self,text="-")
        mins.grid(row =4,column = 3)
        zero = Button(self,text="0")
        zero.grid(row =5 ,column=0)

        dot = Button(self,text=".")
        dot.grid(row =5, column=1 )
        pls = Button(self,text = "+")
        pls.grid(row =5 ,column=2)
        equal = Button(self,text="=")
        equal.grid(row =5,column=3)
        self.pack()
def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()