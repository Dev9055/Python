#ques4
input_num = int(input("Enter a number: "))

if input_num % 3 == 0 and input_num % 5 == 0:
    print("The number {} is divisible by both 3 and 5.".format(input_num))
else:
    print("The number {} is not divisible by both 3 and 5.".format(input_num))

