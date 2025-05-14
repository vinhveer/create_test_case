// Thuật trâu (brute-force, đúng tuyệt đối, không quan tâm tốc độ)
//
// Ý tưởng: Thử tất cả các độ dài l từ 1 đến max(a[i]).
// Với mỗi l, đếm tổng số đoạn cắt được (sum a[i] // l).
// Trả về giá trị l lớn nhất mà tổng số đoạn >= K.
//
// Độ phức tạp: O(max(a[i]) * N) --> chỉ dùng cho test nhỏ/thử nghiệm.

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
    long long ans = 0;
    for (long long l = 1; l <= maxlen; ++l) {
        long long cnt = 0;
        for (int i = 0; i < N; ++i) {
            cnt += a[i] / l;
        }
        if (cnt >= K) ans = l;
    }
    cout << ans << endl;
    return 0;
}