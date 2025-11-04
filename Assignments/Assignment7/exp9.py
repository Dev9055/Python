tup1=(1, 2, 3, 4, 1, 2, 1, 4, 5)
l=[]
for i in tup1:
    if i not in l:
        count=tup1.count(i)
        print("{}: {}".format(i,count))
        l.append(i)
tup2=tuple(l)
