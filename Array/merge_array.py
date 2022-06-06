def merge(m_plus_n, n, size_m, size_n):
    i = size_n # current index of i/p part of m_plus_n[]
    j = 0      # current index of n[]
    k = 0      # cureent index of m_plus_n[]
    
    while (k < (size_m + size_n)):
        if ((j == size_n) or (i < (size_m + size_n) and m_plus_n[i] <= n[j])):
            m_plus_n[k] = m_plus_n[i]
            i += 1
        else:
            m_plus_n[k] = n[j]
            j += 1
        k += 1


def move_to_end(m_plus_n, size): # func to move m elements at the end of array m_plus_n[]
    i = 0
    j = size - 1

    for i in range(size-1, -1, -1):
        if m_plus_n[i] != -1:
            m_plus_n[j] = m_plus_n[i]
            j -= 1


def main():
    m_plus_n = [2, 8, -1, -1, -1, 13, -1, 15, 20]
    n = [5, 7, 9, 25]

    size_n = len(n)
    size_m = len(m_plus_n) - size_n

    move_to_end(m_plus_n, size_n + size_m)
    merge(m_plus_n, n, size_m, size_n)
    print(m_plus_n)


if __name__ == "__main__":
    main()
