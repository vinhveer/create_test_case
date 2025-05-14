// Thuật trâu: Liệt kê mọi cách chèn +, -, hoặc không chèn gì giữa các chữ số
// Độ dài S < 10 nên số trạng thái là 3^(n-1) (n là độ dài S, n-1 vị trí chèn)
// Với mỗi trạng thái, sinh biểu thức, tính giá trị, nếu đúng thì lưu lại.
// Đảm bảo đúng tuyệt đối.

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

typedef long long ll;

// Sinh tất cả các cách chèn +, -, hoặc không chèn gì giữa các chữ số
int main() {
    string S;
    int M;
    cin >> S >> M;
    int n = S.size();
    int total = pow(3, n-1); // 3^(n-1) cách chèn
    vector<string> results;

    // Mỗi vị trí giữa S[i] và S[i+1] có 3 lựa chọn: không gì (nối số), '+', '-'
    // Ta encode mỗi trạng thái thành số base-3
    for (int mask = 0; mask < total; ++mask) {
        string expr;
        expr += S[0];
        int x = mask;
        for (int i = 1; i < n; ++i) {
            int op = x % 3; // 0: nối, 1: '+', 2: '-'
            x /= 3;
            if (op == 1) expr += '+';
            else if (op == 2) expr += '-';
            expr += S[i];
        }

        // Tính giá trị biểu thức expr
        // Duyệt từng ký tự, cộng/trừ theo dấu
        ll val = 0;
        ll cur = 0;
        int sign = 1;
        for (size_t i = 0; i < expr.size(); ) {
            // Xác định dấu
            if (expr[i] == '+') {
                sign = 1;
                ++i;
            } else if (expr[i] == '-') {
                sign = -1;
                ++i;
            }
            // Lấy 1 số liên tiếp
            ll num = 0;
            while (i < expr.size() && isdigit(expr[i])) {
                num = num * 10 + (expr[i] - '0');
                ++i;
            }
            val += sign * num;
        }
        if (val == M) {
            results.push_back(expr);
        }
    }
    cout << results.size() << endl;
    for (auto& s : results) cout << s << endl;
    return 0;
}