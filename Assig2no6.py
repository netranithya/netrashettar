def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # Initialize a matrix to store the lengths of common substrings
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Variables to store the length of the longest common substring and its ending position
    max_length = 0
    end_pos = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_pos = i
            else:
                matrix[i][j] = 0

    return str1[end_pos - max_length: end_pos]

# Example strings
string1 = input("Enter the first string: ")
string2 = input("Enter the Second string: ")

# Finding the longest common substring
result = longest_common_substring(string1, string2)

print(f"The longest common substring is: '{result}'")
