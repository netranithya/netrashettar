def count_unique_chars(string):
    # Using a set to store unique characters
    unique_chars = set(string)
    return len(unique_chars)

input_string = input("Enter the String : ")
result = count_unique_chars(input_string)
print(f"The number of characters in the string is:{result}")