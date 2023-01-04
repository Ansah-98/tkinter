from tkinter import Tk,BOTH
from tkinter.ttk import Frame

class Example(Frame):
    def __init__(self,parent,):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=True)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()