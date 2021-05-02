class computer:
    def __init__(x,processor,RAM):
        x.processor=processor
        x.RAM=RAM
    def getspecs(x):
        x.processor=input("enter processor details")
        x.RAM=input("enter RAM details")
    def displayspecs(x):
        print("processor details is:",x.processor)
        print("RAM details is:",x.RAM)


class desktop(computer):
    def __init__(x,system_id):
        x.system_id=system_id
    def special(x):
        x.system_id=input("enter system id")
        print("system id is:",x.system_id)


class laptop(computer):
    def __init__(x,type):
        x.type=type
    def spec(x):
        x.type=input("enter system type")
        print("system type is:",x.type)


obj=computer("","")
obj.getspecs()
obj.displayspecs()
obj1=desktop("")
obj1.special()
obj2=laptop("")
obj2.spec()





