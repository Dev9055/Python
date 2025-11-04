mixed_tuple=(1,2,3,4,5,1,2,3)
x=[]
for a in mixed_tuple:
    if a not in x:
        x.append(a)
unique_tuple=tuple(x)
print("Tuple of unique elements:{}".format(unique_tuple))
