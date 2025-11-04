list1=[]
n=int(input("enter number of elements in list: "))
print("enter the element of lists: ")
for i in range(n):
    p=int(input())
    list1.append(p)
print("list: ",list1)
list1.reverse()
print("reverse list :",list1)
