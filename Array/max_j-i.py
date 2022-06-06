"""
Given an array arr[], find the maximum
j - i such that arr[j] > arr[i]
"""
def func(arr, size):
    count = float('-inf')

    for i in range(size):
        for j in range(size):
            if arr[j] > arr[i]:
                count = max(count, j - i)

    if count == float('-inf'):
        return -1
    else:
        return count


def max_index_diff(arr, size):
    l_min = [0]*size
    r_max = [0]*size

    l_min[0] = arr[0]
    r_max[size-1] = arr[size-1]

    for i in range(1, size):
        l_min[i] = min(l_min[i-1], arr[i])
    
    for j in range(size-2, -1, -1):
        r_max[i] = max(r_max[j+1], arr[j])

    max_diff, i, j = float('-inf'), 0, 0

    while (j < size and i < size):
        if (l_min[i] <= r_max[j]):
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1
    
    if max_diff == float('-inf'):
        return -1
    else:
        return max_diff


def main():
    # arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    # arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    arr = [1, 2, 3, 4, 5, 6]
    # arr = [6, 5, 4, 3, 2, 1]
    size = len(arr)
    print(func(arr, size))


if __name__ == "__main__":
    main()
