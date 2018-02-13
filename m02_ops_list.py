#!/usr/bin/env python3

# list indexing
some_primes = [2, 3, 5, 7, 3, 7]
prime_set = set(some_primes)
first_prime = some_primes[0]
last_prime = some_primes[-1]
# How about p = prime_set[0]?

# 2D list
pixels = [
    [0, 128, 255],
    [111, 253, 10],
    [20, 31, 100]
]
mid_pixel = pixels[1][1]
print(pixels, mid_pixel)


prime_list = list(prime_set)
print('Unsorted:', prime_list)
# Sort in place. You can use sorted() too
prime_list.sort()
print('Sorted:', prime_list)

# Slice: start index = 0 (inclusive), end index = 2 (exclusive)
first_two = prime_list[0:2] # same as prime_list[:2]
last_two = prime_list[-2:]

# Concatenate, '+' operator works almost universally (duck typing)
first_and_last_two = first_two + last_two
print('first_two:', first_two, 'last_two:', last_two, 'first_and_last_two:', first_and_last_two)

print('prime_list before append:', prime_list)
# Append another value
prime_list.append(11)
print('prime_list after append:', prime_list)

# or "append" another list
prime_list.extend(last_two)
print('prime_list after extend:', prime_list)
