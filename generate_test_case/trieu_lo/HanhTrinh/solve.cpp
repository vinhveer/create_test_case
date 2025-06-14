#include <iostream>
#include <vector>
using namespace std;

int countPaths(const vector<vector<int>>& adj, int u, int v, int k) {
    if (k == 0) return u == v ? 1 : 0;

    int count = 0;
    for (int i = 0; i < adj.size(); i++) {
        if (adj[u][i]) {
            count += countPaths(adj, i, v, k - 1);
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> adj(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> adj[i][j];

    int k, v_i, v_j;
    cin >> k >> v_i >> v_j;

    int result = countPaths(adj, v_i, v_j, k);
    cout << result << endl;

    return 0;
}
