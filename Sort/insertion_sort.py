import numpy as np
import time

def insertion_sort(arr):
    res = []
    if len(arr) != 0:
        res.append(arr[0])
        for i in range(1, len(arr)):
            for j in range(len(res)):
                if arr[i] < res[j]:
                    res.insert(j, arr[i])
                    break
                elif j == i-1:
                    res.append(arr[i])
    return res
    
if __name__ == '__main__':
    # generate data
    np.random.seed(233)
    array = np.random.randint(10000, size=10000)
    
    # calculate execution time
    prev_time = time.time()
    sorted_array = insertion_sort(array)
    exec_time = time.time() - prev_time
    
    # assertion
    assert(sorted_array == [sorted(array)])
    print(exec_time)
    