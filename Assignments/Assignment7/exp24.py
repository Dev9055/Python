tuple1=(1,2,3,4)
tuple2=(3,4,5,6)
l=[]
for i in tuple1:
    if i in tuple2:
        l.append(i)
t=tuple(l)
print("Intersection of tuple1 and tuple2 is:{}".format(t))
