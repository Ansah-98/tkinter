import random
from tkinter import Button, Tk , BOTH,LEFT,RIGHT,X,Y,StringVar
from tkinter.ttk import Frame,Label

class myRandom(object):
    def __init__(self):
        self.r = 0
    
    def generate(self):
        self.r = random.randint(0,99) 
    
    def getrandom(self):
        return self.r

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent )
        self.parent = parent 
        self.mr = myRandom()
        self.initUi()

    def initUi(self):
        self.parent.title("custom event ")
        self.pack(fill=BOTH, expand=True)


        self.parent.bind("<<Random>>", self.updateLabel )
        btn = Button(self,text="Random" ,command= self.onclick)
        btn.grid(row=0 ,column=0, padx=10,pady=10)

        self.Ivar = StringVar()

        lbl = Label(self,textvariable = self.Ivar)
        lbl.grid(row =0 ,column=1 ,padx =50)

    def onclick(self):
        self.mr.generate()
        self.event_generate("<<Random>>")


    def updateLabel(self,e):

        self.Ivar.set(self.mr.getrandom())
def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()