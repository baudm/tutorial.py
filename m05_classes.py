#!/usr/bin/env python3

class Layer(object):

    def __init__(self):
        self.weights = 0.1
        self.input = None

    def __call__(self, *args, **kwargs):
        print('call', args, kwargs)

    def forward(self, input):
        self.input = input
        output = self.weights * input
        return output

    def backward(self, doutput):
        gradient = doutput * self.input
        return gradient


def main():
    layer = Layer()
    o = layer.forward(10)
    print(o)

    g = layer.backward(0.5)
    print(g)

    layer(1, 2, input_shape=(3, 2), output_shape=(2,))


if __name__ == '__main__':
    main()
