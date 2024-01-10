rows = 6  # Number of rows in the pyramid
num = 1   # Starting number

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
        if num > 20:  # Adjust the upper limit if needed
            break
    print()
    if num > 20:
        break
