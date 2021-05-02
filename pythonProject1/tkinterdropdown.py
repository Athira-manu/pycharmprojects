# from tkinter import*
# root=Tk()
# def fun():
#     print("hai")
#
# mymenu=Menu(root)
# root.config(menu=mymenu)
# submenu=Menu(mymenu)
# mymenu.add_cascade(label="file",menu=submenu)
# submenu.add_command(label="save",command=fun)
# submenu.add_separator()
# submenu.add_command(label="exit",command=root.quit)
#
# newmenu=Menu(mymenu)
# mymenu.add_cascade(label="edit",menu=newmenu)
# newmenu.add_command(label="undo")
# newmenu.add_command(label="redo")
#
# root.mainloop()







from tkinter import*
root=Tk()
def fun():
    print("hello")
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(labe="file",menu=submenu)
submenu.add_command(label="save",command=fun)
submenu.add_separator()
submenu.add_command(label="new")
newmenu=Menu(mymenu)
mymenu.add_cascade(labe="edit",menu=newmenu)
newmenu.add_command(label="undo")
newmenu.add_separator()
newmenu.add_command(label="redo")

root.mainloop()





















