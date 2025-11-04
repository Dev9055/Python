nested_tuple=((1,2),(3,4),(5,6))
l=[]
for i in nested_tuple:
        l.extend(i)
t=tuple(l)
print("Flattened Tuple:{}".format(t))
