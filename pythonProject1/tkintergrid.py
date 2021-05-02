# from tkinter import*
# root=Tk()
# Label(root,text="username").grid(row=0,column=0)
# Entry(root).grid(row=1,column=0)
# Label(root,text="password").grid(row=2,column=0)
# Entry(root).grid(row=3,column=0)
# Button(root,text="login").grid(row=4,column=0)
# root.mainloop()


from tkinter import*
root=Tk()
def fun():
    print("u r successfully logged in")
Label(root,text="username").grid(row=0,column=0)
Entry(root).grid(row=1,column=0)
Label(root,text="password").grid(row=2,column=0)
Entry(root).grid(row=3,column=0)
Button(root,text="login",command=fun).grid(row=4,column=0)
root.mainloop()