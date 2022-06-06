def segregate(arr, size):
    left = 0
    right = size - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1
        if left < right and arr[left] == 1 and arr[right] == 0:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1


def main():
    arr = [0, 1, 0, 1, 1, 1]
    size = len(arr)
    segregate(arr, size)
    print(arr)


if __name__ == "__main__":
    main()