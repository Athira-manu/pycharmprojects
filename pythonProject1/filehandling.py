file1=open("demo.txt","r")
c=file1.read()
print(c)
file1.close()

file1=open("demo.txt","a")
file1.write("\nhai avodha")
file1.close()


# file=open("xyz.txt","w")
# file.write("hello")
# file.write("hai")
# file.close()


# file=open("xyz.txt","a")
# file.write("what r u doing")
# file.close()