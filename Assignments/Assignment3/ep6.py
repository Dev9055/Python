_type=input("type of tringle: ")
a=int(input("enter the side a of triangle: "))
b=int(input("enter the side b of triangle: "))
c=int(input("enter the side c of triangle: "))
s=(a+b+c)//2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("type of triangle=",_type)
print("area of triangle =",area)
