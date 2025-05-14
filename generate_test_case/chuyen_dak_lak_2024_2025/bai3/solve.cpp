/*
Giải thích thuật tối ưu:
- N là số chữ số của P (rất lớn), S là tập các chữ số cấm (không có 0).
- Xây dựng số lớn nhất <= P mà không chứa chữ số cấm, không có số 0 ở đầu.
- Ý tưởng: Duyệt từng chữ số của P từ trái sang phải, tại mỗi vị trí cố gắng chọn số lớn nhất <= P[i] (nếu ở trạng thái còn "tight"), nhưng không thuộc S.
- Nếu không chọn được, lùi lại vị trí trước, giảm đi 1 và chọn số lớn nhất không cấm, sau đó điền các số lớn nhất không cấm ở các vị trí tiếp theo.
- Nếu không thể chọn được (cấm hết tất cả số), in -1.

Độ phức tạp: O(N) với N là số chữ số của P.
*/

#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
    string P, S;
    cin >> P >> S;
    set<char> forbidden(S.begin(), S.end());
    int N = P.size();
    string res = "";
    bool found = false;

    // Precompute allowed digits (không cấm, không 0 ở đầu)
    string allowed = "";
    for (char d = '9'; d >= '0'; --d) {
        if (!forbidden.count(d)) allowed += d;
    }
    if (allowed.empty() || (allowed.size() == 1 && allowed[0] == '0')) {
        cout << -1 << endl;
        return 0;
    }

    // Greedy, backtrack khi cần
    for (int i = 0; i < N; ++i) {
        char best = -1;
        // Nếu chưa từng "bẻ" nhỏ hơn P[i], cố chọn số lớn nhất <= P[i] (và không cấm)
        // Nếu đã từng bẻ nhỏ rồi, chọn số lớn nhất không cấm (và không 0 ở đầu)
        char start = (i == 0 ? '1' : '0');
        for (char d = P[i]; d >= start; --d) {
            if (!forbidden.count(d)) {
                if (d < P[i]) {
                    // Chọn d < P[i], sau đó điền các số lớn nhất không cấm
                    res += d;
                    for (int j = i+1; j < N; ++j) {
                        for (char x = '9'; x >= '0'; --x)
                            if (!forbidden.count(x)) {
                                res += x;
                                break;
                            }
                    }
                    cout << res << endl;
                    return 0;
                }
                best = d;
                break;
            }
        }
        if (best == -1) {
            // Không chọn được số nào ở vị trí này, phải lùi lại vị trí trước
            int j = i-1;
            while (j >= 0) {
                char cur = res[j];
                char next_best = -1;
                for (char d = cur-1; d >= (j == 0 ? '1' : '0'); --d) {
                    if (!forbidden.count(d)) {
                        next_best = d;
                        break;
                    }
                }
                if (next_best != -1) {
                    res = res.substr(0, j) + next_best;
                    // Điền các số lớn nhất không cấm cho các vị trí sau
                    for (int k = j+1; k < N; ++k) {
                        for (char x = '9'; x >= '0'; --x)
                            if (!forbidden.count(x)) {
                                res += x;
                                break;
                            }
                    }
                    cout << res << endl;
                    return 0;
                }
                j--;
            }
            cout << -1 << endl;
            return 0;
        }
        res += best;
    }
    // Nếu tới đây, res là số cùng số chữ số với P, không nhỏ hơn P, cần kiểm tra <=P
    if (res <= P) cout << res << endl;
    else {
        // Phải lùi lại để chọn số nhỏ hơn
        int j = N-1;
        while (j >= 0) {
            char cur = res[j];
            char next_best = -1;
            for (char d = cur-1; d >= (j == 0 ? '1' : '0'); --d) {
                if (!forbidden.count(d)) {
                    next_best = d;
                    break;
                }
            }
            if (next_best != -1) {
                res = res.substr(0, j) + next_best;
                for (int k = j+1; k < N; ++k) {
                    for (char x = '9'; x >= '0'; --x)
                        if (!forbidden.count(x)) {
                            res += x;
                            break;
                        }
                }
                cout << res << endl;
                return 0;
            }
            j--;
        }
        cout << -1 << endl;
    }
    return 0;
}