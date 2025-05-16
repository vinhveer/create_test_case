#include <bits/stdc++.h>
using namespace std;

// Brute-force: sinh hoán vị, áp dụng với m <= 8
// Nếu m > n: không gán hết áo, không đúng đề bài, nhưng theo đề thì m <= n luôn (m áo, n ma-nơ-canh)

int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<int>> V(m, vector<int>(n));
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            cin >> V[i][j];

    // Nếu m > 8 thì quá lớn, báo lỗi, chỉ chạy brute-force cho m <= 8
    if (m > 8) {
        cout << "Brute-force chỉ áp dụng cho m <= 8\n";
        return 0;
    }

    vector<int> perm(n);
    for (int i = 0; i < n; ++i) perm[i] = i;

    int ans = -1;
    vector<int> best;
    do {
        int sum = 0;
        for (int i = 0; i < m; ++i)
            sum += V[i][perm[i]];
        if (sum > ans) {
            ans = sum;
            best = vector<int>(perm.begin(), perm.begin() + m);
        }
    } while (next_permutation(perm.begin(), perm.end()));

    cout << ans << "\n";
    for (int i = 0; i < m; ++i) {
        cout << best[i] + 1 << (i == m-1 ? '\n' : ' ');
    }
    return 0;
}