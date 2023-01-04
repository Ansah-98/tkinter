from tkinter import Tk ,BOTH
from tkinter.ttk import Frame, Label , Notebook,Style
from tkinter.font import Font


class FontExample(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUi()
    

    def initUi(self):
        self.parent.title("font for tkinter apps")
        self.pack(fill= BOTH, expand= True)

        txt ='tkinter is default python gui library'

        myfont = Font(family="Ubuntu Mono"  , size = 16)
        label1  = Label(self, text= txt ,font=  myfont)
        label1.grid(row = 0,column =0)

        label2 = Label(self, text=txt , font= 'TktestFont')
        label2.grid(row= 1, column =0)

        label3  = Label(self,text = txt , font = ('Times', '18', 'italic'))
        label3.grid(row = 2 , column= 0)

def main():
    root = Tk()
    app = FontExample(root)
    app.initUi()
    root.mainloop()

if __name__ == '__main__':
    main()