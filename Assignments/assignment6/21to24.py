lst=[]
n=int(input('Enter the number of elements of list: '))
print('Enter the elements of list(string): ')
for i in range(n):
    p=str(input())
    lst.append(p)
print('List 1:',lst)
lst.sort()
print('Alphabetical order sorted list:',lst)
#22
lst=[]
n=int(input('Enter the number of elements of list: '))
print('Enter the elements of list: ')
for i in range(n):
    p=int(input())
    lst.append(p)
print('List 1:',lst)
m=int(input('Enter the number you want to remove:'))
i=0
while i<len(lst):
    if lst[i]==m:
        del lst[i]
    else:
        i=i+1
print('New list :',lst)
#23
l1=[]
l=int(input("Enter length of list1:"))
for i in range(0,l):
    e=int(input())
    l1.append(e)
print("List:",l1)
sl=[i**2 for i in l1 if i%2==0]
print("Squared list:",sl)
print('New list :',lst2)
#24
txt=str(input('Enter the elements of list(string): '))
lst=txt.split()
print('List:',lst)
count=0
vowels =['a','e','i','o','u','A','E','I','O','U']
for string in lst:
    for char in string:
        if char in vowels:
            count=count+1
    
print('Vowels: ',count)
