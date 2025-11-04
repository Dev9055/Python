#1
tuple1=(5,8,2)
tuple2=(3,6,1)
#2
result_tuple=tuple1+tuple2
#3
l=list(result_tuple)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]>l[j]:
            x=l[i]
            l[i]=l[j]
            l[j]=x
sorted_tuple=tuple(l)
#4
print("Sorted Tuple: {}".format(sorted_tuple))
