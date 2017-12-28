def sort(nums):
    length = len(nums)
    res = []
    if length > 2:
        mid = int(length/2)
        left_sorted = sort(nums[:mid])
        right_sorted = sort(nums[mid:])
        
        if len(left_sorted) == 0:
            res = right_sorted
        elif len(right_sorted) == 0:
            res = left_sorted
        else:
            left_key = 0
            right_key = 0
            while left_key != len(left_sorted) and right_key != len(right_sorted):
                # list.append(int)
                if left_sorted[left_key] < right_sorted[right_key]:
                    res.append(left_sorted[left_key])
                    left_key += 1
                else:
                    res.append(right_sorted[right_key])
                    right_key += 1

            # list.extend(list) 
            if left_key == len(left_sorted):
                res.extend(right_sorted[right_key:])
            else:
                res.extend(left_sorted[left_key:])

    elif length == 2:
        res = [min(nums), max(nums)]
    elif length == 1:
        res = [nums[0]]
    return res