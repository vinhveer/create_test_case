#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    bool directed = false;
    for (long long i = 0; i < n && !directed; i++) {
        for (long long j = i+1; j < n; j++) {
            if (a[i][j] != a[j][i]) {
                directed = true;
                break;
            }
        }
    }

    long long edges = 0;
    if (directed) {
        for (long long i = 0; i < n; i++) {
            for (long long j = 0; j < n; j++) {
                edges += a[i][j];
            }
        }
    } else {
        long long off_diag = 0, loops = 0;
        for (long long i = 0; i < n; i++) {
            if (a[i][i]) loops += a[i][i];
            for (long long j = i+1; j < n; j++) {
                off_diag += a[i][j];
            }
        }
        edges = off_diag + loops;
    }

    cout << edges << "\n";
    return 0;
}