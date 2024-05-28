l1=[1,2,3,4,5,6]
l2=[for i in l1 if(i%2==0),"even"]
print(l2)
for i in l1:
    if(i%2==0):
        print("even")
    else:
        print("odd")
        l2.append(i)

