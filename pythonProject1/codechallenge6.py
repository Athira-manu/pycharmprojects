file1=open("demo.txt","r")
c=file1.read()
print(c)
file1.close()

file1=open("demo.txt","a")
file1.write("\nhai avodha")
file1.close()