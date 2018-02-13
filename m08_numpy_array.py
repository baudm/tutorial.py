#!/usr/bin/env python3

import numpy as np

PATCH_3x3 = np.array([
    [255, 127, 31],
    [4, 0, 55],
    [147, 203, 100]
])


def main():
    print(PATCH_3x3)
    print(PATCH_3x3.shape)
    print(PATCH_3x3.dtype)


if __name__ == '__main__':
    main()