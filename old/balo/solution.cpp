#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<long long, vector<int>> knapsack(int n, long long W, const vector<long long>& weights, const vector<long long>& values) {
    // Initialize dp table
    vector<vector<long long>> dp(n + 1, vector<long long>(W + 1, 0));
    
    // Fill dp table
    for (int i = 1; i <= n; ++i) {
        for (long long j = 0; j <= W; ++j) {
            if (weights[i-1] > j) {
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1]);
            }
        }
    }
    
    // Trace back to find selected items
    vector<int> selected;
    int i = n;
    long long j = W;
    while (i > 0 && j > 0) {
        if (dp[i][j] != dp[i-1][j]) {
            selected.push_back(i);
            j -= weights[i-1];
        }
        --i;
    }
    reverse(selected.begin(), selected.end());
    
    return {dp[n][W], selected};
}

int main() {
    int n;
    long long W;
    cin >> n >> W;
    
    vector<long long> weights(n), values(n);
    for (int i = 0; i < n; ++i) {
        cin >> weights[i] >> values[i];
    }
    
    auto [max_value, selected] = knapsack(n, W, weights, values);
    
    cout << max_value << endl;
    if (!selected.empty()) {
        for (size_t i = 0; i < selected.size(); ++i) {
            if (i > 0) cout << " ";
            cout << selected[i];
        }
        cout << endl;
    }
    
    return 0;
}