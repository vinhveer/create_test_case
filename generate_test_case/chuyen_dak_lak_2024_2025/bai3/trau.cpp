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

    // Chuẩn bị tập allowed
    string allowed = "";
    for (char d = '9'; d >= '0'; --d)
        if (!forbidden.count(d)) allowed += d;
    if (allowed.empty() || (allowed.size() == 1 && allowed[0] == '0')) {
        cout << -1 << endl;
        return 0;
    }

    int i = 0;
    bool smaller = false; // đã chọn số nhỏ hơn P
    while (i < N) {
        char start = (i == 0 ? '1' : '0');
        char best = -1;
        for (char d = (smaller ? '9' : P[i]); d >= start; --d) {
            if (!forbidden.count(d)) {
                if (!smaller && d < P[i]) {
                    res += d;
                    for (int j = i+1; j < N; ++j)
                        for (char x = '9'; x >= '0'; --x)
                            if (!forbidden.count(x)) { res += x; break; }
                    cout << res << endl;
                    return 0;
                }
                if (!smaller && d == P[i]) {
                    best = d;
                    break;
                }
                if (smaller) {
                    res += d;
                    break;
                }
            }
        }
        if (!smaller && best != -1) {
            res += best;
        } else if (!smaller && best == -1) {
            // cần lùi về trước
            int j = i-1;
            while (j >= 0) {
                char cur = res[j];
                char next_best = -1;
                for (char d = cur-1; d >= (j == 0 ? '1' : '0'); --d)
                    if (!forbidden.count(d)) { next_best = d; break; }
                if (next_best != -1) {
                    res = res.substr(0, j) + next_best;
                    for (int k = j+1; k < N; ++k)
                        for (char x = '9'; x >= '0'; --x)
                            if (!forbidden.count(x)) { res += x; break; }
                    cout << res << endl;
                    return 0;
                }
                j--;
            }
            cout << -1 << endl;
            return 0;
        } else if (smaller) {
            break;
        }
        i++;
    }
    if (!res.empty()) {
        cout << res << endl;
        return 0;
    }
    cout << -1 << endl;
    return 0;
}