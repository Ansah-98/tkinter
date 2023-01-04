"""

managing widgets in parent window using the place layout manager 

"""
from tkinter import Tk,BOTH
from tkinter.ttk import Frame,Label,Style
from PIL import Image,ImageTk
class Place(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.parent.title(" managing with place ")
        self.pack( fill=BOTH , expand = True)

        s = Style()
        s.configure("TFrame", background = "#333")

        img1  = Image.open("")
        img_p  = ImageTk.PhotoImage(img1)
        label1 = Label(self ,image = img_p)
        label1.image  =  img_p  
        label1.place(x =20,y = 20)

        img2  = Image.open('')
        img2_p = ImageTk.PhotoImage(img2)
        label2   = Label(self,image=img2_p)
        label2.image = img2_p
        label2.place(x=40,y =160)

def main():
    root = Tk()
    root.geometry('300x300+250+100')
    win = Place(Frame)
    root.mainloop()

if __name__ == '__main__':
    main()
    