def mandelbrot(x, y, max):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < max:
        z = z**2 + c
        it += 1
    return it
