str1=input("Enter a sentence: ")
lst1=str1.split()
lst2=[]
for i in lst1:
 if i not in lst2:
     count=lst1.count(i)
     print("{}: {}".format(i,count))
     lst2.append(i)
