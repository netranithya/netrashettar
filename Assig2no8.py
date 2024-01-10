def check_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Example usage:
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if check_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
