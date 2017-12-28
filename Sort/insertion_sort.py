def sort(arr):
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