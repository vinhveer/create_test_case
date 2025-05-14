#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Trả về số lớn nhất có thể tạo thành là dãy giảm dần từ S (giữ đúng thứ tự, có thể bỏ ký tự)
string max_decreasing(const string& S) {
    string best = "";
    int n = S.size();
    // Với xâu <= 18 ký tự, liệt kê mọi tập con ~2^18 (~260k), chấp nhận được cho thuật trâu!
    // Nếu n > 18, chỉ kiểm thử test nhỏ
    int N = min(n, 18);
    for (int mask = 1; mask < (1 << N); ++mask) {
        string cur = "";
        char last = '9'+1;
        for (int i = 0; i < N; ++i) {
            if (mask & (1 << i)) {
                if (cur.empty() || S[i] < cur.back())
                    cur += S[i];
                else
                    break;
            }
        }
        if (cur.size() > best.size() || (cur.size() == best.size() && cur > best))
            best = cur;
    }
    // Nếu n > 18, kiểm tra các dãy đơn lẻ từ vị trí 18 trở đi
    for (int i = 18; i < n; ++i) {
        string cur = "";
        cur += S[i];
        for (int j = i+1; j < n; ++j) {
            if (S[j] < cur.back())
                cur += S[j];
        }
        if (cur.size() > best.size() || (cur.size() == best.size() && cur > best))
            best = cur;
    }
    return best;
}

int main() {
    string S;
    cin >> S;
    cout << max_decreasing(S) << endl;
    return 0;
}