class power:
    def cal_power(self,x,n):
        return x**n
cal=power()
x=int(input("enter the value of x: "))
n=int(input("enter the value of n: "))
result=cal.cal_power(x,n)
print("output={}".format(result))

