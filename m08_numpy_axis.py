#!/usr/bin/env python3

import m08_numpy_array as array


def main():
    patch = array.PATCH_3x3
    global_mean = patch.mean()
    row_mean = patch.mean(axis=-1)
    row_mean_same_dims = patch.mean(axis=-1, keepdims=True)
    print(patch)
    print(global_mean)
    print(row_mean)
    print(row_mean_same_dims)


if __name__ == '__main__':
    main()