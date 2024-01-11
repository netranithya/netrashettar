def find_duplicates(list1, list2, list3):
    # Concatenate all three lists
    combined_list = list1 + list2 + list3

    # Initialize an empty set to store duplicates
    duplicates = set()
    seen = set()

    for item in combined_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = find_duplicates(list1, list2, list3)

if result:
    print("Duplicate elements in the three lists:", result)
else:
    print("No duplicates found in the three lists.")
