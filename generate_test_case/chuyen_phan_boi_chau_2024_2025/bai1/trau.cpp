#include <iostream>
using namespace std;

// Hàm kiểm tra một số có đúng 4 ước số dương hay không
bool is_special(int x) {
    int cnt = 0;
    for (int i = 1; i*i <= x; ++i) {
        if (x % i == 0) {
            cnt++;
            if (i != x/i) cnt++;
        }
        if (cnt > 4) return false;
    }
    return cnt == 4;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--) {
        int L, R;
        cin >> L >> R;
        int ans = 0;
        for (int x = L; x <= R; ++x)
            if (is_special(x)) ++ans;
        cout << ans << '\n';
    }
    return 0;
}