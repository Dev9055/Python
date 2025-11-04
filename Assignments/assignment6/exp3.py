a=input("enter string:")
vowels="aeiouAEIOU"
i=0
for char in a:
    if char in vowels:
        i += 1
print("number of vowels: {} ".format(i))
