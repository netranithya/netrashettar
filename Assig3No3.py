def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def find_happy_numbers_in_list(lst):
    happy_numbers = [num for num in lst if is_happy_number(num)]
    return happy_numbers

# Example usage:
input_list = [10,501,22,37,100,999,87,351]
result = find_happy_numbers_in_list(input_list)

if result:
    print("Happy numbers in the list:", result)
else:
    print("No happy numbers found in the list.")
