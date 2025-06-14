#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int INF = 1000000000;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    int start;
    cin >> start;

    vector<int> dist(n, INF);
    vector<int> parent(n, -1);
    vector<bool> used(n, false);

    dist[start] = 0;
    parent[start] = start;

    // Dijkstra O(n^2)
    for (int count = 0; count < n; count++) {
        int u = -1;
        int min_dist = INF;
        for (int i = 0; i < n; i++) {
            if (!used[i] && dist[i] < min_dist) {
                min_dist = dist[i];
                u = i;
            }
        }
        if (u == -1) break;
        used[u] = true;
        for (int v = 0; v < n; v++) {
            // Nếu trọng số > 0 và chưa xét
            if (matrix[u][v] > 0 && dist[u] + matrix[u][v] < dist[v]) {
                dist[v] = dist[u] + matrix[u][v];
                parent[v] = u;
            }
        }
    }

    // Hàm dựng đường đi (vốn từ parent)
    auto getPath = [&](int v) {
        vector<int> path;
        while (true) {
            path.push_back(v);
            if (parent[v] == v || parent[v] == -1) break;
            v = parent[v];
        }
        reverse(path.begin(), path.end());
        return path;
    };

    // Xuất kết quả
    for (int i = 0; i < n; i++) {
        if (dist[i] < INF) {
            auto path = getPath(i);
            // Chuyển path thành dạng "a->b->c"
            string path_str;
            for (int j = 0; j < (int)path.size(); j++) {
                path_str += to_string(path[j]);
                if (j + 1 < (int)path.size()) {
                    path_str += "->";
                }
            }
            cout << i << "|" << dist[i] << "|" << path_str << "\n";
        }
    }

    return 0;
}