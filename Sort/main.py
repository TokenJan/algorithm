import insertion_sort
import merge_sort
import numpy as np
import time

if __name__ == '__main__':
    # generate data
    np.random.seed(233)
    array = np.random.randint(10000, size=10000)
    
    # calculate execution time
    prev_time = time.time()
    sorted_array = merge_sort.sort(array)
    exec_time = time.time() - prev_time
    
    # assertion
    assert(sorted_array == sorted(array))
    print(exec_time)