def first_non_repeating_element(lst):
    element_count = {}

    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    for element in lst:
        if element_count[element] == 1:
            return element

    return None  # Return None if no non-repeating element is found


# Example usage:
input_list = [3,4, 2, 6, 8, 2, 4, 9, 6]

result = first_non_repeating_element(input_list)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found in the list.")
