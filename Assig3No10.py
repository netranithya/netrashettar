def find_sublist_with_sum_zero(nums):
    prefix_sum = 0
    sum_set = set()
    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in sum_set:
            return True
        sum_set.add(prefix_sum)
    return False

# Example usage:
given_list = [4, 2, -3, 1, 6]

if find_sublist_with_sum_zero(given_list):
    print("Sublist with sum 0 exists.")
else:
    print("No sublist with sum 0 found.")
