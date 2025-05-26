#include<bits/stdc++.h>
using namespace std;
#include <bits/stdc++.h>
using namespace std;

const int MAX = 1e5 + 5;
int n, m, a[MAX], b[MAX];

int distance_range(int l, int r) {
    return r - l + 1;
}

int main() {
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    // #endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    // Đọc mảng a[1..n]
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // Đọc mảng b[1..m]
    cin >> m;
    for (int i = 1; i <= m; ++i) {
        cin >> b[i];
    }

    // Tìm __left: vị trí cuối cùng mà a vẫn không giảm (từ trái sang)
    int __left = n;
    for (int i = 2; i <= n; ++i) {
        if (a[i] < a[i - 1]) {
            __left = i - 1;
            break;
        }
    }

    // Tìm __right: vị trí đầu tiên từ phải qua mà b vẫn không tăng
    int __right = 1;
    for (int i = m - 1; i >= 1; --i) {
        if (b[i] > b[i + 1]) {
            __right = i + 1;
            break;
        }
    }

    // Ghép hai prefix-suffix sao cho a[1..i] ≤ b[__right..m]
    int res = 0;
    bool flag = true;
    for (int i = 1; i <= __left; ++i) {
        // đẩy __right cho đến khi b[__right] ≥ a[i]
        while (a[i] > b[__right]) {
            ++__right;
            if(__right>m){
                flag=false;
                break;
            }
        }
        if(!flag)
            break;
        // i là độ dài prefix, distance_range(__right, m) là độ dài suffix
        res = max(res, i + distance_range(__right, m));
    }

    cout << res << '\n';
    return 0;
}
