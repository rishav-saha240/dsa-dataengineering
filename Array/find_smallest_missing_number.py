def find_smallest_missing_number(arr, size):
    if arr[0] != 0:
        return 0

    for i in range(1, size-1, 1):
        if arr[i+1] - arr[i] > 1:
            return arr[i]+1
    
    return -1


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
    size = len(arr)
    ans = find_smallest_missing_number(arr, size)
    if ans == -1:
        print("No missing number")
    else:
        print(f"Missing number is: {ans}")


if __name__ == "__main__":
    main()
