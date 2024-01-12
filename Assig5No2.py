my_list = [333, 777, 9, 'GUVI', 'ZEN']

check_and_print = lambda x: print(f"{x} is an integer") if isinstance(x, int) else print(f"{x} is a string")

# Use map to apply the lambda function to each element in the list
list(map(check_and_print, my_list))
