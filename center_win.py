from tkinter import Tk ,BOTH
from tkinter.ttk import Frame

class Center(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent  = parent
        self.initUi()
        self.centerW()

    def initUi(self):
        self.parent.title('centering window')
        self.pack(fill = BOTH, expand=True)
    
    def centerW(self):
        w = 290
        h = 150

        sx =  self.parent.winfo_screenwidth()
        sy = self.parent.winfo_screenheight()

        x= int((sx-w)/2)
        y = int((sy-h)/2)

        self.parent.geometry(f"{w}x{h}+{x}+{y}")
def main():
    root = Tk()
    app = Center(root)
    root.mainloop()

if __name__ == "__main__":
    main()