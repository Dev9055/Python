n=int(input("enter the number: "))
flag=0
for i in range(1,n):
    if i*i==n:
        flag=1
        break
if flag==0:
    print("its not a perfect square")
else:
    print("its a perfect square")
    
