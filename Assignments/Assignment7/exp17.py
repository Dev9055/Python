students=(("Alice", 22), ("Bob", 19), ("Charlie",25))
l=list(students)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i][1]<l[j][1]:
            x=l[i]
            l[i]=l[j]
            l[j]=x
sorted_tuple=tuple(l)
print("Sorted Tuple: {}".format(sorted_tuple))
