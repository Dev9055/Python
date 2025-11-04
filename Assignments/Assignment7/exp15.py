#1
test_tuple=(1,2,3,4,5)
#2
num=int(input("Enter a number:"))
#3
if num in test_tuple:
    print("{} is in tuple".format(num))
else:
    print("{} is not in tuple".format(num))
