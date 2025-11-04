def string_test(input_string):
    count_dict = {'upper': 0, 'lower': 0, 'space': 0}
    for char in input_string:
        if char.isupper():
            count_dict['upper'] += 1
        elif char.islower():
            count_dict['lower'] += 1
        elif char.isspace():
            count_dict['space'] += 1
    return count_dict

def main():
    input_string = input("Enter any sentence: ")
    result = string_test(input_string)
    print("\nOriginal String: ", input_string)
    print("No. of Upper case characters: ", result['upper'])
    print("No. of Lower case Characters: ", result['lower'])
    print("No. of spaces: ", result['space'])

main()
