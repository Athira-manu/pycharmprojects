dic={"soap":50,"shampoo":70,"kajal":75}
c=input("enter a product name:")
for i in dic:
     if i==c:
        print("price of the item is:",dic[i])
        break
else:
    print("not found")

