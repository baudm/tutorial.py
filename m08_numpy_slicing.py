#!/usr/bin/env python3

import m08_numpy_array as array


def main():
    patch = array.PATCH_3x3.copy()
    col0 = patch[:, 0]
    col1 = patch[:, 1]
    col2 = patch[:, 2]
    print(patch, '\n')
    print('col0:', col0, '\n')
    print('col1:', col1, '\n')
    print('col2:', col2, '\n')

    # Zero out the middle column
    patch[:, 1] = 0
    print('patch:', patch)

    # Set all values >= 100 to 1
    patch[patch >= 100] = 1
    print('patch:', patch)

    mask = patch > 0
    print('mask:', mask)


if __name__ == '__main__':
    main()