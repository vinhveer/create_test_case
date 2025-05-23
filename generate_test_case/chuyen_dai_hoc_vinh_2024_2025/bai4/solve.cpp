#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> grid(n+1, vector<int>(m+1));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> grid[i][j];
        }
    }
    
    // We'll use two 1D arrays to reduce memory and speed up computations
    vector<int> dpPrev(n+1, -1e9), dpCur(n+1, -1e9);
    
    // Initialize dp for the first column
    for (int i = 1; i <= n; i++) {
        dpPrev[i] = grid[i][1];
    }
    
    // Fill the DP table column by column
    for (int j = 2; j <= m; j++) {
        for (int i = 1; i <= n; i++) {
            int val1 = dpPrev[i];
            int val2 = (i > 1) ? dpPrev[i-1] : -1e9;
            int val3 = (i < n) ? dpPrev[i+1] : -1e9;
            dpCur[i] = grid[i][j] + max({val1, val2, val3});
        }
        dpPrev.swap(dpCur);
    }
    
    // Find the maximum value in the last column
    cout << *max_element(dpPrev.begin()+1, dpPrev.end()) << "\n";
    return 0;
}
