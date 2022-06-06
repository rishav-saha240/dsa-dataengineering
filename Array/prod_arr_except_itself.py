def product_arr(arr, size):
    if size == 1:
        print(0)
        return
    
    left = [1]*size
    right = [1]*size
    prod = [1]*size
    left[1] = 1
    right[size-1] = 1

    for i in range(1, size):
        left[i] = arr[i-1] * left[i-1]
    # print(left)
    for j in range(size-2, -1, -1):
        right[j] = arr[j+1] * right[j+1]
    # print(right)
    for i in range(size):
        prod[i] = left[i] * right[i]

    return prod

def main():
    arr = [10, 3, 5, 6, 2]
    size = len(arr)
    print(product_arr(arr, size))
    

if __name__ == "__main__":
    main()