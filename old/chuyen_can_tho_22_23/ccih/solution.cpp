#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    // Đọc số nguyên n dưới dạng chuỗi để có thể xử lý cả khi |n| > 10^18
    if (!(cin >> s)) return 0;

    int best = 0;
    for (char c : s) {
        if (isdigit(c)) {
            best = max(best, c - '0');
            // Nếu đã gặp 9 thì không thể lớn hơn nữa, thoát sớm
            if (best == 9) break;
        }
    }

    cout << best << "\n";
    return 0;
}
