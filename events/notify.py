"""the following event shows a small notification window 
    it works with these two events <button-1> and <buttonRelease-1>

"""

from tkinter import Tk,BOTH,Toplevel,messagebox
from tkinter.ttk import Frame ,Label,Style
import time

class NotifyWindow(Toplevel):
    def __init__(self,parent,elasped,screenx ,screeny):
        Toplevel.__init__(self,parent ,background = "sky blue")
        self.overrideredirect(True)
        self.el = elasped
        self.screenx = screenx
        self.screeny = screeny


        self.initUi()

    def initUi(self):
        s= Style()
        s.configure("TLabel",background= 'sky blue')

        lbl = Label(self, text = str(self.el) + "ms")
        lbl.pack(pady = 5, padx=5)
        self.update()

        h =self.winfo_height()
        self.geoometry(f"{ self.screenx}x{(self.screeny - h)}")
        self.after(self.el ,self.destroyWin)

    def destroyWin(self):
        self.destroy()
    
class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent 
        self.initUi()
    

    def initUi(self):
        self.parent.title("Notify")
        self.pack(fill= BOTH, expand=True)

        self.bind("<Button-1>" , self.onPress)
        self.bind("<ButtonRelease-1>" , self.onRelease)

    def onPress(self):
        print("true")
        self.start = time.time()
    
    def onRelease(self, e):

        screenx = e.x_root
        screeny = e.y_root
        
        self.stop = time.time()
        el = self.stop - 0
        el_ms = el* 1000 
        el_r = round(el_ms)
        self.createNotificationWindow(el_r,screenx ,screeny)
    
    def createNotificationWindow(self,elapsed,screenx,screeny):
        nwin = NotifyWindow(self,elapsed,screenx,screeny)
    

def main():
    root = Tk()
    root.geometry("350x250+300+300")

    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()