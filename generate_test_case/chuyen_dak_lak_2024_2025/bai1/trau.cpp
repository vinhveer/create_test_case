// Thuật trâu: Đếm với từng số từ 1 tới N xem có chia hết cho 3 hoặc 5 không. Đúng tuyệt đối, dùng cho N nhỏ (<=1e6).

#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N;
        cin >> N;
        int cnt = 0;
        for (long long i = 1; i <= N; ++i) {
            if (i % 3 == 0 || i % 5 == 0) cnt++;
        }
        cout << cnt << endl;
    }
    return 0;
}