class student:
    def __init__(self,name,hodname,subject):
        self.name=name
        self.hodname=hodname
        self.subject=subject
    def getdata(self):
        self.name=input("enter the name")
        self.hodname=input("enter hod name")
        self.subject=input("enter subject name")


class hod(student):
    def display(self):
        print("the name is",self.name)
        print("hod name is",self.hodname)
        print("subject name is",self.subject)

class C(hod):
    def fun(self):
        print("class c")
class D(C):
    def fun1(self):
        print("class d")


obj=D("","","")
obj.getdata()
obj.display()
obj.fun()
obj.fun1()
