class student:
    def __init__(x,name,mark):
        x.name=name
        x.mark=mark
    def get(x):
        x.name=input("enter the name")
        x.mark=input("enter the mark")
        print(x.name,"\n",x.mark)
obj=student('','')
obj.get()