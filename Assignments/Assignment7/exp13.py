#1
num_tuple = (10, 20, 30, 40, 50)
#2
max_element = num_tuple[0]
for num in num_tuple:
    if num > max_element:
        max_element = num
#3
print("Maximum Element:", max_element)
