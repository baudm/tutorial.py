#!/usr/bin/env python3

def stub():
    # TODO: implement this
    pass


def repeat_element(element, reps=2, **kwargs):
    out = [element] * reps
    print('kwargs:', kwargs)
    return out


def p(tag, *args):
    print(tag, args)


def main():
    elements = repeat_element(1)
    print('elements:', elements)

    elements2 = repeat_element(3, 5)
    print('elements2:', elements2)

    elements3 = repeat_element(1, reps=3, nothing='really')
    print('elements3:', elements3)

    p('DEBUG:', 1, 2, 3, 4)


if __name__ == '__main__':
    main()
