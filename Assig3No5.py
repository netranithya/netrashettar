def distribute_mangoes(mango_bags, students):
    mango_bags.sort()

    min_difference = float('inf')

    for i in range(len(mango_bags) - students + 1):
        max_mangoes = mango_bags[i + students - 1]
        min_mangoes = mango_bags[i]
        difference = max_mangoes - min_mangoes

        if difference < min_difference:
            min_difference = difference

    return min_difference


# Example usage:
mango_bags = [3, 7, 2, 10, 1]
students = 3

min_diff = distribute_mangoes(mango_bags, students)

print("Minimum difference between the number of mangoes in bags:", min_diff)
