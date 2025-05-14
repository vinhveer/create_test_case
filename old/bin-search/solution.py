def binary_search(a, x):
    left, right = 0, len(a) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            result = mid
            right = mid - 1  # Tiếp tục tìm bên trái
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1 if result == -1 else result + 1  # Chỉ số 1-based

if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    result = binary_search(a, x)
    print(result)
