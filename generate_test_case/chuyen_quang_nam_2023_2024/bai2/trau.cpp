#include <bits/stdc++.h>
using namespace std;

// Thuật trâu: Duyệt tất cả số chính phương <= max(a_i), kiểm tra có trong dãy không, cộng dồn nếu không có

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    long long maxv = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        maxv = max(maxv, a[i]);
    }

    // Đánh dấu các số xuất hiện
    unordered_set<long long> exist;
    for (int i = 0; i < n; ++i) exist.insert(a[i]);

    // Duyệt các số chính phương <= maxv
    long long sum = 0;
    for (long long k = 0; ; ++k) {
        long long sq = k*k;
        if (sq > maxv) break;
        if (exist.find(sq) == exist.end()) sum += sq;
    }
    cout << sum << '\n';
    return 0;
}