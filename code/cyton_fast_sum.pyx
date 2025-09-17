# my_module.pyx
def fast_sum(long long[:] arr):
    cdef long long total = 0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total