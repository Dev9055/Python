n = int(input("Enter the value of n: "))
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f"Sum of even numbers from 1 to {n}: {even}")
print(f"Sum of odd numbers from 1 to {n}: {odd}")
