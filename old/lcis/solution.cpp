#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, vector<long long>> lcis(const vector<long long>& a, const vector<long long>& b) {
    int n = a.size();
    int m = b.size();
    // dp[i][j]: độ dài LCIS khi xét đến a[i-1] và b[j-1]
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    // prev[i][j]: lưu vị trí trước đó trong a và b để truy vết
    vector<vector<pair<int, int>>> prev(n + 1, vector<pair<int, int>>(m + 1, {-1, -1}));

    int max_len = 0;           // Độ dài LCIS tối đa
    pair<int, int> end_pos = {-1, -1}; // Vị trí kết thúc của LCIS tối đa

    // Tính bảng dp và lưu thông tin truy vết
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i-1] == b[j-1]) {
                dp[i][j] = 1;  // Bắt đầu một LCIS mới
                prev[i][j] = {-1, -1};
                // Kiểm tra các phần tử trước để nối dài LCIS
                for (int k = 0; k < i - 1; ++k) {
                    if (a[k] < a[i-1]) {
                        for (int l = 0; l < m; ++l) {
                            if (b[l] == a[k] && dp[k+1][l+1] + 1 > dp[i][j]) {
                                dp[i][j] = dp[k+1][l+1] + 1;
                                prev[i][j] = {k, l};
                            }
                        }
                    }
                }
            }
            // Cập nhật LCIS tối đa
            if (dp[i][j] > max_len) {
                max_len = dp[i][j];
                end_pos = {i-1, j-1};
            }
        }
    }

    // Truy vết để xây dựng LCIS
    vector<long long> lcis_seq;
    int i = end_pos.first;
    int j = end_pos.second;
    while (i >= 0 && j >= 0 && prev[i+1][j+1].first != -1) {
        lcis_seq.push_back(a[i]);
        auto [prev_i, prev_j] = prev[i+1][j+1];
        i = prev_i;
        j = prev_j;
    }
    if (i >= 0 && j >= 0) {
        lcis_seq.push_back(a[i]);
    }
    reverse(lcis_seq.begin(), lcis_seq.end());

    return {max_len, lcis_seq};
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }

    auto [len, seq] = lcis(a, b);

    cout << len << endl;
    if (len > 0) {
        for (size_t i = 0; i < seq.size(); ++i) {
            if (i > 0) cout << " ";
            cout << seq[i];
        }
        cout << endl;
    }

    return 0;
}