#!/usr/bin/env python3

import math

def is_prime(num):
    if num == 1:
        return False

    s = math.sqrt(num)
    if (num % 2 == 0 and 2 <= s) or (num % 3 == 0 and 3 <= s):
        return False

    # All primes, except 2 and 3, are of the form 6k +/- 1
    # Thus, only integers of this form, up to sqrt(num),
    # are needed for the primality test.
    for p in range(5, int(math.ceil(s)), 6):
        if num % p == 0 or num % (p + 2) == 0:
            return False

    return True


def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i


def main():
    for p in prime_generator(20):
        print(p)


if __name__ == '__main__':
    main()
