def find_triplet_with_sum(nums, target_sum):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target_sum:
                    return [nums[i], nums[j], nums[k]]
    return None

# Example usage:
given_list = [10, 20, 30, 9]
target_sum = 59

triplet = find_triplet_with_sum(given_list, target_sum)

if triplet is not None:
    print("Triplet with sum {} found: {}".format(target_sum, triplet))
else:
    print("No triplet found with sum {}.".format(target_sum))
