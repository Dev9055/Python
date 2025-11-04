num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
num3=int(input("enter num3 :"))
if num1 >= num2:
    if num1 >= num3:
        print("the greatest is = {}".format(num1))
elif num2 >= num1:
    if num2 >= num3:
        print("the greatest is = {}".format(num2))
    else :
        print("the greatest is = {}".format(num3))
