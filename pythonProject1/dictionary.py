dic={"a":10,"b":20,"c":30}
print(dic)
for i in dic.items():
    print(i)
print (dic["a"])
del(dic["b"])
print(dic)
dic["a"]=40
print(dic)