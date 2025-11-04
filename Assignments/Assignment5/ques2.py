list={70,50,40,89,90}
num=int(input("Enter a number to be found :"));
if num in list:
    print("{} is in list".format(num))
else:
    print("{} is not in the list".format(num))

if num not in list:
    print("{} is not in the list".format(num))
else:
    print("{} is in the list".format(num))
