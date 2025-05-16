#include <bits/stdc++.h>
using namespace std;

// Hàm in ra kết quả theo yêu cầu đề bài
void solve(const string &S) {
    vector<int> digits;
    for (char c : S) {
        if (isdigit(c)) digits.push_back(c - '0');
    }
    if ((int)digits.size() < 6) {
        cout << "-1\n";
        return;
    }

    // DP trâu: dp[i][k] = xâu lớn nhất chọn k số từ digits[i..]
    int n = digits.size();
    vector<vector<string>> dp(n+1, vector<string>(7, "")); // chỉ cần 0..6
    for (int i = n; i >= 0; --i) {
        for (int k = 0; k <= 6; ++k) {
            if (k == 0) {
                dp[i][k] = ""; // không chọn số nào
            } else if (i == n) {
                dp[i][k] = "-"; // không đủ số để chọn
            } else {
                // Chọn hoặc không chọn digits[i]
                string take = dp[i+1][k-1];
                if (take != "-") take = to_string(digits[i]) + take;
                string skip = dp[i+1][k];
                // So sánh 2 xâu, lấy xâu lớn hơn
                if (take == "-") dp[i][k] = skip;
                else if (skip == "-") dp[i][k] = take;
                else dp[i][k] = (take > skip ? take : skip);
            }
        }
    }
    string res = dp[0][6];
    if (res == "-") cout << "-1\n";
    else {
        cout << res << "\n";
        int sum = 0;
        for (char c : res) sum += c - '0';
        cout << sum << "\n";
    }
}

int main() {
    string S;
    getline(cin, S);
    solve(S);
    return 0;
}