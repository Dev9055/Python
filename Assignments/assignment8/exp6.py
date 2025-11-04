class Even_Odd:
    def check(self, number):
        if number % 2 == 0:
            return "number is even."
        else:
            return "number is odd."

x = Even_Odd()
num = int(input("Enter a number: "))

result = x.check(num)
print(result)
