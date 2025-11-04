str1 = input("Enter a string: ")
lst=str1.split()
count=0
for i in lst:
    lst[count]=i.capitalize()
    count+=1

str2=' '.join(lst)
print(str2)
