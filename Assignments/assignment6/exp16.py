lst=[]
lst2=[]
n=int(input('Enter the number of elements of first list: '))
print('Enter the elements of first list: ')
for i in range(n):
    p=int(input())
    lst.append(p)

m=int(input('Enter the number of elements of second list: '))
print('Enter the elements of second list: ')
for i in range(m):
    q=int(input())
    lst2.append(q)
print('List 1:',lst)
print('List 2:',lst2)
lst3=[x for x in lst if x in lst2]
lst3.sort()
print('Intersected (common) element in both list:',lst3)
