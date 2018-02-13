#!/usr/bin/env python3

import importlib
import m01_intro


def main():
    print(m01_intro.mapping)
    d = m01_intro.mapping
    d['new_key'] = 1
    print(d)
    print(m01_intro.mapping)

    importlib.reload(m01_intro)
    print(m01_intro.mapping)


if __name__ == '__main__':
    main()
