def sum_first_and_last_digit(number):
    # Convert the number to a string to extract digits
    num_str = str(number)

    # Check if the number has only one digit
    if len(num_str) == 1:
        return int(num_str)

    # Calculate the sum of the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    return first_digit + last_digit


# Example usage:
input_number = int(input("Enter a number: "))
result = sum_first_and_last_digit(input_number)
print("Sum of the first and last digit:", result)
