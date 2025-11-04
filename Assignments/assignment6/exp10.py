str1=input("Enter a string: ")
lst=list(str1)
count=0
for i in lst:
    a=lst.count(i)
    if a>1:
        print("False")
        count=0
        break
    else:
        count+=1

if count>0:
    print("True")
