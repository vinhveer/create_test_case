def merge(a, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    # Hợp nhất hai dãy con đã sắp xếp
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    # Sao chép phần còn lại của nửa trái (nếu có)
    while i <= mid:
        temp.append(a[i])
        i += 1

    # Sao chép phần còn lại của nửa phải (nếu có)
    while j <= right:
        temp.append(a[j])
        j += 1

    # Sao chép từ mảng tạm về mảng chính
    for k in range(len(temp)):
        a[left + k] = temp[k]

def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)

# Hàm chính
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    merge_sort(a, 0, n - 1)

    print(" ".join(map(str, a)))
