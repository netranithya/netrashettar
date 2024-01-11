def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_list(lst):
    prime_numbers = [num for num in lst if is_prime(num)]
    return prime_numbers

# Example usage:
input_list = [10,501,22,37,100,999,87,351]
result = find_primes_in_list(input_list)

if result:
    print("Prime numbers in the list:", result)
else:
    print("No prime numbers found in the list.")
