#Question 2: Tuple Manipulation
#1
original_tuple=(10, 20, 30, 40, 50)
#2
print("length of original_tuple: ",len(original_tuple))
#3
print("the element at index 3: ",original_tuple[3])
#4
print("the last element of the tuple: ",original_tuple[-1])
#5
new_list=list(original_tuple)
#6
new_list.append(60)
#7
new_tuple=tuple(new_list)
#8
print("new_tuple: ",new_tuple)
