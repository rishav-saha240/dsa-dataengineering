def find_duplicates(arr, size):
    for i in range(size):
        x = arr[i] % size
        arr[x] = arr[x] + size

    print(arr)


def main():
    arr = [0, 4, 3, 2, 7, 8, 2, 3, 1]
    size = len(arr)
    find_duplicates(arr, size)


if __name__ == "__main__":
    main()
