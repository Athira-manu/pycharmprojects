import re
# p=r"avodha"
# if re.match(p,"avodha hai"):
#     print("matched")
# else:
#     print("not matched")

# if re.search(p,"hai  how are you avodha"):
#     print("matched")
# else:
#     print("not matched")

# print(re.findall("avodha","fhgfdghgavodhacvbnavodhartytyuuiavodhadfghjavodha"))

# x=re.sub("avodha","AVODHA","hai avodha how are you avodha")
# print(x)

p=r"av.d.ha"
if re.match(p,"avodnha"):
    print("yes")
else:
    print("no")

x=r"[a-z][A-Z][0-9]"
if re.search(x,"rQ4"):
    print("correct")
else:
    print("not correct")