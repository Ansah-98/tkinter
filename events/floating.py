"""this app is used to create a floating window without any title bar"""


from tkinter import BitmapImage, Toplevel


class Example(Toplevel):
    def  __init__(self,parent):
        Toplevel.__init__(self,parent) 
        self.initUi()



    def initUi(self):
        self.overrideredirect(True)
        bitMap = BitmapImage(data = BITMAP)