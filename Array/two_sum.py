def has_array_two_candidate(arr, n):
    left = 0
    right = len(arr) - 1

    while (left < right):
        if (arr[left] + arr[right]) == n:
            return 1
        elif (arr[left] + arr[right]) < n:
            left += 1
        else:
            right -= 1
    return 0


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        (i, j, k) = (0, 0, 0)

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        

def main():
    # arr = [1, 4, 45, 6, 10, -8]
    arr = [1, -2, 1, 0, 5]
    n = 0
    merge_sort(arr)
    if (has_array_two_candidate(arr, n) == 1):
        print("Pair exists")
    else:
        print("Pair doesn't exists")


if __name__ == "__main__":
    main()