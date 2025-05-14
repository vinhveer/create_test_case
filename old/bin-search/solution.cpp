#include <iostream>
#include <vector>

using namespace std;

// Tìm kiếm nhị phân để tìm vị trí đầu tiên của x
int binary_search(const vector<long long>& a, long long x) {
    int left = 0, right = a.size() - 1;
    int result = -1; // Lưu vị trí đầu tiên tìm thấy

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == x) {
            result = mid; // Ghi nhận vị trí, nhưng tiếp tục tìm bên trái
            right = mid - 1;
        } else if (a[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result == -1 ? -1 : result + 1; // Chuyển sang chỉ số 1-based
}

int main() {
    int n;
    long long x;
    cin >> n >> x;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // Gọi tìm kiếm nhị phân
    int result = binary_search(a, x);

    // In kết quả
    cout << result << endl;

    return 0;
}