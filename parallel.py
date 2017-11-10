import numpy as np
import time
from matplotlib import pyplot
from mpi4py import MPI

from mandelbrot import mandelbrot

t0 = time.time()
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a = 2
b = 2
height = 200
width = 300
max_iter = 150

default_local_height = height // size
local_height = default_local_height
if rank == size:
    local_height = height - default_local_height * (size - 1)
local_array_len = local_height * width
local_result = np.zeros(shape=[local_array_len],
                        dtype='i')

dx = a / height
dy = b / width
for row in range(local_height):
    shift = default_local_height * rank
    y = -b / 3 + (row + shift) * dy
    for col in range(width):
        x = -a + col * dx
        local_result[col + row * width] = mandelbrot(x, y, max_iter)
print('{0} process for {1} seconds'.format(rank, time.time() - t0))
local_result.shape = (local_height, width)
pyplot.imshow(local_result, aspect='equal')
pyplot.spectral()
pyplot.show()
result = None
if rank == 0:
    result = np.empty([height * width], dtype='i')
comm.Gather(sendbuf=local_result,
            recvbuf=result,
            root=0)
if rank == 0:
    result.shape = (height, width)
    print('all time for execution {}'.format(time.time() - t0))
    pyplot.imshow(result, aspect='equal')
    pyplot.spectral()
    pyplot.show()
