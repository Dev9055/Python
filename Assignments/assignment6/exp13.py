lst=[]
n=int(input('Enter the number of elements: '))
print('Enter the elements of list: ')
for i in range(n):
    p=int(input())
    lst.append(p)
print('List:',lst)
s=0
for i in range(0,len(lst)):
    s=s+lst[i]
print('Sum of element in list :',s)
