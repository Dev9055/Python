num = int(input("Enter the number of terms for the Fibonacci series: "))
first= 0
second= 1
sum=0
if num<=0:
    print("enter num greater then 0: ")
else:
    for i in range(0, num):
        print(sum,end=" ")
        first=second
        second=sum
        sum= first+second
