#include <iostream>
#include <vector>

using namespace std;

// Hàm hợp nhất hai dãy con đã sắp xếp
void merge(vector<long long>& a, int left, int mid, int right) {
    // Tạo mảng tạm để lưu kết quả hợp nhất
    vector<long long> temp(right - left + 1);
    int i = left;      // Chỉ số cho nửa trái
    int j = mid + 1;   // Chỉ số cho nửa phải
    int k = 0;         // Chỉ số cho mảng tạm

    // Hợp nhất hai dãy con
    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
        }
    }

    // Sao chép phần còn lại của nửa trái (nếu có)
    while (i <= mid) {
        temp[k++] = a[i++];
    }

    // Sao chép phần còn lại của nửa phải (nếu có)
    while (j <= right) {
        temp[k++] = a[j++];
    }

    // Sao chép từ mảng tạm về mảng chính
    for (int p = 0; p < k; ++p) {
        a[left + p] = temp[p];
    }
}

// Hàm Merge Sort đệ quy
void merge_sort(vector<long long>& a, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2; // Tính chỉ số giữa
        merge_sort(a, left, mid);           // Sắp xếp nửa trái
        merge_sort(a, mid + 1, right);      // Sắp xếp nửa phải
        merge(a, left, mid, right);         // Hợp nhất hai nửa
    }
}

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // Gọi Merge Sort
    merge_sort(a, 0, n - 1);

    // In kết quả
    for (int i = 0; i < n; ++i) {
        if (i > 0) cout << " ";
        cout << a[i];
    }
    cout << endl;

    return 0;
}