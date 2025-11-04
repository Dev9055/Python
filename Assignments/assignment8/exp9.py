def perfect(number):
    sum = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            if i * (number // i) == number:
                sum += i + number // i
            i += 1
    return (sum == number and number != 1)

def perfect_numbers(N):
    perfect_numbers_list = []
    for i in range(1, N + 1):
        if perfect(i):
            perfect_numbers_list.append(i)
    return perfect_numbers_list

N = int(input("Enter the value of N: "))
print("Perfect numbers are: ", perfect_numbers(N))
