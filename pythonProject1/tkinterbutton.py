from tkinter import*
root=Tk()
f=Frame(root)
f.pack()

def fun():
    print("hai")
def fun1():
    print("you are signed in")
Button(f,text="login",bg="orange",command=fun).pack()
Button(f,text="sign in",bg="blue",command=fun1).pack()
root.mainloop()
