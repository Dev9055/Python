a=input("Enter the first string: ")
b=input("Enter the second string: ")
x=[i for i in a]
x.sort()

y=[j for j in b]
y.sort()


if x==y:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
