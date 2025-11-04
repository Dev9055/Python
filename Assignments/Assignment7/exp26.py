range_tuple=(10,20,30,40,50)
n=int(input("Enter a number:"))
max=0
for i in range_tuple:
    if i>max:
        max=i
min=max
for i in range_tuple:
    if i<min:
        min=i
if min<=n<=max:
    print("The number is in range")
else:
    print("The number is not in range")
