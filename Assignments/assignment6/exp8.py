string=input('Enter String For String Compression:')
com=[]
c=1
for i in range(1,len(string)):                                               
    if string[i]==string[i-1]:
        c+=1
    else:
        com.append(string[i-1]+str(c))
        c=1
com.append(string[-1]+str(c))
s=''.join(com)
print(s)

            
