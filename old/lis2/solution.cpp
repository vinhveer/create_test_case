#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void generateLIS(int pos, int len, vector<long long>& a, vector<vector<int>>& prev, vector<long long>& current, vector<vector<long long>>& result) {
    if (len == 0) {
        result.push_back(current);
        return;
    }
    for (int j : prev[pos]) {
        current.push_back(a[j]);
        generateLIS(j, len - 1, a, prev, current, result);
        current.pop_back();
    }
}

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // dp[i]: độ dài LIS kết thúc tại chỉ số i
    vector<int> dp(n, 1);
    // prev[i]: danh sách các chỉ số j mà a[j] có thể đứng trước a[i] trong LIS
    vector<vector<int>> prev(n);

    // Tìm LIS
    int maxLen = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] < a[i] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i].clear();
                prev[i].push_back(j);
            } else if (a[j] < a[i] && dp[j] + 1 == dp[i]) {
                prev[i].push_back(j);
            }
        }
        if (dp[i] == 1 && prev[i].empty()) {
            prev[i].push_back(-1); // Không có phần tử trước
        }
        maxLen = max(maxLen, dp[i]);
    }

    // Tìm tất cả chỉ số kết thúc của LIS
    vector<int> endIndices;
    for (int i = 0; i < n; ++i) {
        if (dp[i] == maxLen) {
            endIndices.push_back(i);
        }
    }

    // Tạo tất cả các dãy con tăng dài nhất
    vector<vector<long long>> result;
    vector<long long> current;
    for (int i : endIndices) {
        current.push_back(a[i]);
        generateLIS(i, maxLen - 1, a, prev, current, result);
        current.pop_back();
    }

    // Sắp xếp các dãy theo thứ tự từ điển
    sort(result.begin(), result.end());

    // In kết quả
    cout << maxLen << endl;
    cout << result.size() << endl;
    for (const auto& lis : result) {
        for (long long x : lis) {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}