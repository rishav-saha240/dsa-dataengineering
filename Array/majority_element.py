def find_majority(arr, size):
    m = {}
    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    for key, value in m.items():
        if value > size//2:
            print(f"Majority element is : {key}")
            return 
    print("No majority element found")


def main():
    # arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
    arr = [1, 2, 3, 4, 5]
    size = len(arr)
    find_majority(arr, size)


if __name__ == "__main__":
    main()