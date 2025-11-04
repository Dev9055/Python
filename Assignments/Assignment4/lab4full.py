dash='-'
#1.
n=int(input('Enter a number: '))
print(n)
print(dash*90)
#2.
f=float(input('Enter a float number: '))
print('{:.2f}'.format(f))
print(dash*90)
#3.
integer=10
decimal=10.11
num_ber=-5
print(type(integer))
print(type(decimal))
print(type(num_ber))
print(dash*90)
#4
string=str(input('Enter a string: '))
print(string[0])
print(string[3])
print(string[-1])
print(dash*90)
#5
name=str(input('Enter your name: '))
age=int(input('Enter your age: '))
new=('Hi {},you are {} years old!!!'.format(name,age))
print(new)
print(dash*90)
#6
a=str(input('Enter string: '))
b=str(input('Enter second string: '))
c=('I love {} programming, it is very Useful.'.format(a,b))
print(c)
print(dash*90)
#7
x=int(input('enter a number: '))
y=int(input('enter 2nd number: '))
if x>y:
    print("x is greater than y")
else:
    print("y is greater than X")
