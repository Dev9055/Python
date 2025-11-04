tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)
l=[]
for i in tuple1:
    if i in tuple2:
        l.append(i)
t=tuple(l)
if t==tuple1:
    print("Equal")
else:
    print("Not Equal")
    
