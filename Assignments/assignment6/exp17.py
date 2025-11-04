lst=[]
n=int(input('Enter the number of elements of first list: '))
print('Enter the elements of first list: ')
for i in range(n):
    p=int(input())
    lst.append(p)
print('List 1:',lst)
lst2=lst[2:7]
print('Element from 3rd to 6th(inclusive):',lst2)
