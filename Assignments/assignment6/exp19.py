l1=[]
n=int(input("Enter length of list1:"))
for i in range(0,n):
    e=input()
    l1.append(e)
print("List1:",l1)
for i in range(n):
    if i%2==0:
        print(l1[i][::-1])
