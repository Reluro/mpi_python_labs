import numpy
import time
from matplotlib import pyplot

from mandelbrot import mandelbrot


def compute_set(a, b, h=200, w=300, max=150):
    result = numpy.zeros([h, w], dtype='i')
    dx = a / h
    dy = b / w
    for row in range(result.shape[0]):
        y = -b / 3 + row * dy
        for col in range(result.shape[1]):
            x = -a + col * dx
            result[row, col] = mandelbrot(x, y, max)
    return result


t0 = time.time()
if __name__ == "__main__":
    t0 = time.time()
    c = compute_set(a=2, b=2)
    print('{} seconds'.format(time.time() - t0))
    pyplot.imshow(c, aspect='equal')
    pyplot.spectral()
    pyplot.show()
