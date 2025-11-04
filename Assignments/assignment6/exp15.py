lst=[]
n=int(input('Enter the number of elements of first list: '))
print('Enter the elements of first list: ')
for i in range(n):
    p=int(input())
    lst.append(p)
print('List 1:',lst)
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
print('List having unique element:',lst2)
