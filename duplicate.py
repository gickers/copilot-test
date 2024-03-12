def duplicate2(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.extend([arr[i], arr[i]])
    return new_arr
