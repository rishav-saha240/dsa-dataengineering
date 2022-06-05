def print_pairs(arr, sum, size):
    hash_map = {}

    for i in range(size):
        temp = sum - arr[i]
        if (temp in hash_map):
            print(f"Pair with given sum {sum} is ({temp}, {arr[i]}) at indices ({hash_map[temp]}, {i})")
        hash_map[arr[i]] = i


def main():
    arr = [1, 4, 45, 6, 10, 8]
    sum = 16
    print_pairs(arr, sum, len(arr))


if __name__ == "__main__":
    main()