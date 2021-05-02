# x=lambda a,b,c:a+b*c
# print(x(6,5,2))

def fun(n):
    return lambda a:a+n
x=fun(5)
print(x(6))
y=fun(7)
print(y(8))