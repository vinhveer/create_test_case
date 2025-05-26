#include <bits/stdc++.h>
using namespace std;

const int MAX = 1e6 + 5;
int a[MAX], cnt[MAX];
int n, k;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];
    cin >> k;

    for (int i = 1; i <= n; ++i) {
        int sum = 0;
        for (int j = i; j <= n; ++j) {
            sum += a[j];
            if (k % sum == 0)
                ++cnt[sum];
        }
    }

    int ans = 0;
    for (int i = 1; i <= k; ++i) {
        if (k % i == 0) {
            ans += cnt[i] * cnt[k / i];
        }
    }

    cout << ans << '\n';

    return 0;
}
