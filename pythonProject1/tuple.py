t=("apple","orange","mango")
print(t)
for i in t:
    print(i)
if "apple" in t:
    print("yes")
y=list(t)
y[1]="papaya"
t=tuple(y)
print(t)
print(len(t))
t1=(1,2,3,4)
print(t+t1)
t2=(1,1,2,3,3,3,2,4,5,5)
print(t2.count(1))