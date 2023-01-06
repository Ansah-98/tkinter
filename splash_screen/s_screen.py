
"""  the script creates splash before starting the main application  """

from tkinter import Toplevel,PhotoImage,BOTH,Tk
from tkinter.ttk import Frame ,Label,Button

class MySplash(Toplevel):
    def __init__(self,parent):
        Toplevel.__init__(self)

        self.delay = 3000
        self.parent = parent 
        self.initUi()

    def initUi(self):
        self.splash_image  = PhotoImage(file  = "splash.png")
        w = self.splash_image.width()
        h = self.splash_image.height()

        self.overrideredirect(True)

        x = (self.parent.winfo_screenwidth()-w)/2
        y = (self.parent.winfo_screenheight()-h)/2

        self.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

        self.splash_label = Label(self,image=self.splash_image)
        self.splash_label.pack()

        self.after(self.delay,self.close)

    def close(self):
        self.parent.buildApp()
        self.destroy()
class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,name="frame")
        self.parent = parent 
        self.initUi()

    def initUi(self):
        self.pack(fill=BOTH,expand=True)
        self.parent.title("Application")
        self.parent.withdraw()
        self.showSplashScreen()
    
    def buildApp(self):
        self.quitButton = Button(self, text = "Quit", command = self.quit)
        self.quitButton.pack(padx = 10,pady=10)

        self.parent.deiconify()

    def showSplashScreen(self):
        MySplash(self)

def main():
    root = Tk()
    root.geometry("250x200+300+300")
    app = Example(root)
    root.mainloop()
if __name__ == "__main__":
    main()