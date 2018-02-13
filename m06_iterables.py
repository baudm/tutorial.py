#!/usr/bin/env python3

def main():
    primes = {2, 3, 5, 7, 11}
    pixels = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    message = 'Hello, world!'
    shape = (3, -2, 1)
    loader = (i**2 for i in range(10))
    params = {
        'learning_rate': 0.001,
        'steps_per_epoch': 1000,
        'data': loader
    }

    for p in primes:
        print(p)

    for row in pixels:
        print(row)
        for p in row:
            print(p)

    for c in message:
        print(c)

    for d in shape:
        print(d)

    for k, v in params.items():
        print('key:', k, 'value:', v)


if __name__ == '__main__':
    main()