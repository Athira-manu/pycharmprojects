from tkinter import*
root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
button=Button(root,text="send")
button.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
root.mainloop()