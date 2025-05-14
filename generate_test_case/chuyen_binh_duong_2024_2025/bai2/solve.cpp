/*
Giải thích thuật tối ưu:
- Thuật toán nhị phân đáp án. Độ dài đoạn cắt lớn nhất nằm trong [1, max(a[i])].
- Với mỗi giá trị mid, kiểm tra tổng số đoạn cắt được có >= K không (sum a[i] // mid).
- Nếu có, tăng mid lên; nếu không, giảm mid xuống.
- Đáp án là giá trị lớn nhất thỏa mãn.

Độ phức tạp: O(N log(max(a[i]))), đảm bảo chạy tốt với N, a[i] lớn.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<long long> a(N);
    long long maxlen = 0;
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
        if (a[i] > maxlen) maxlen = a[i];
    }
    long long l = 1, r = maxlen, ans = 0;
    while (l <= r) {
        long long mid = (l + r) / 2;
        long long cnt = 0;
        for (int i = 0; i < N; ++i) cnt += a[i] / mid;
        if (cnt >= K) {
            ans = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    cout << ans << endl;
    return 0;
}