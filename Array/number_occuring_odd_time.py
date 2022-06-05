def get_odd_occurrence(arr, size):
    hash_map = dict()

    for i in range(size):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1

    for i in hash_map:
        if hash_map[i] % 2 != 0:
            return i
    return -1


def main():
    arr = [2, 3, 5, 4, 5, 2, 4,3, 5, 2, 4, 4, 2]
    size = len(arr)
    ans = get_odd_occurrence(arr, size)
    if ans != -1:
        print(f"Odd occurring element: {ans}")
    else:
        print("No odd occurring number")


if __name__ == "__main__":
    main()
