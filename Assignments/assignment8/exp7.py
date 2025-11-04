def convert_to_uppercase(word_list):
    uppercase_list = [word.upper() for word in word_list]
    return uppercase_list
list_input = input("Enter words separated by commas: ").split(',')

list_input = [word.strip() for word in list_input]

uppercase = convert_to_uppercase(list_input)

print("Uppercase words:", uppercase)
