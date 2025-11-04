#23
l1=[]
l=int(input("Enter length of list1:"))
for i in range(0,l):
    e=int(input())
    l1.append(e)
print("List:",l1)
sl=[i**2 for i in l1 if i%2==0]
print("Squared list:",sl)
#24
txt=str(input('Enter the elements of list(string): '))
lst=txt.split()
print('List:',lst)
count=0
vowels ='AEIOUaeiou'
for string in lst:
    for char in string:
        if char in vowels:
            count=count+1
    
print('Vowels: ',count)

#25


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
merge=lst+lst2
n = len(merge)
for i in range(n):
    for j in range(0, n-i-1):
        if merge[j] > merge[j+1]:
                merge[j], merge[j+1] = merge[j+1], merge[j]
print('New list :',merge)

