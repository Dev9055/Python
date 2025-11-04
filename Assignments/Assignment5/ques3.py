str1=str(input("Enter any word: "))
print(str1)
search=str(input("Enter any chracter to be founded in word :"))
if search in str1:
    print("The character is present")
else:
    print("The chracter is not present")
