#1
check_tuple=(10, 20, 30, 40, 50)
#2
num_check=int(input("enter number you want to check :"))
#3
if num_check in check_tuple:
    print("number {} present in tuple".format(num_check))
else:
    print("number {} not present in tuple".format(num_check))
