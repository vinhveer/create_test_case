#include <bits/stdc++.h>
using namespace std;

// Thuật trâu brute-force: duyệt mọi đoạn con, kiểm tra điều kiện
int main() {
    int N, M;
    cin >> N >> M;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    long long res = 0;
    for (int l = 0; l < N; ++l) {
        for (int r = l; r < N; ++r) {
            // kiểm tra đoạn [l, r] có ít nhất 1 phần quà >= M
            bool ok = false;
            for (int k = l; k <= r; ++k) {
                if (a[k] >= M) {
                    ok = true;
                    break;
                }
            }
            if (ok) ++res;
        }
    }
    cout << res << "\n";
    return 0;
}