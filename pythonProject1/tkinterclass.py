from tkinter import*
root=Tk()
class demo():
    def __init__(self,x):
        frame=Frame(x)
        frame.pack()
        Button(frame,text="hello",command=self.printmsg).pack()
        Button(frame,text="exit",command=frame.quit).pack()
    def printmsg(self):
        print("hai how r u?")
obj=demo("")

root.mainloop()