#!/usr/bin/env python3

import numpy as np
import m08_numpy_array as array

def main():
    normalized = array.PATCH_3x3 / 255.
    print(normalized)
    print(normalized.shape)
    print(normalized.dtype)

    mean_intensities = np.array([0.5, 0.25, 0.], dtype=normalized.dtype)
    centered = normalized - mean_intensities
    print(centered)
    print(centered.shape)
    print(centered.dtype)


if __name__ == '__main__':
    main()
