#include <bits/stdc++.h>
using namespace std;

static const int DIRS[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

struct DSU
{
    vector<int> parent, size;
    DSU(int n) : parent(n), size(n, 1)
    {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    int findp(int v)
    {
        if (parent[v] == v)
            return v;
        return parent[v] = findp(parent[v]);
    }
    void unite(int a, int b)
    {
        a = findp(a);
        b = findp(b);
        if (a != b)
        {
            if (size[a] < size[b])
                swap(a, b);
            parent[b] = a;
            size[a] += size[b];
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    cin >> m >> n;
    vector<vector<int>> grid(m, vector<int>(n));
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> grid[i][j];
        }
    }

    // DSU approach: label each land cell, union connected ones
    DSU dsu(m * n);
    auto idx = [&](int r, int c)
    { return r * n + c; };

    // Union all connected land cells
    for (int r = 0; r < m; r++)
    {
        for (int c = 0; c < n; c++)
        {
            if (grid[r][c] == 1)
            {
                for (auto &d : DIRS)
                {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1)
                    {
                        dsu.unite(idx(r, c), idx(nr, nc));
                    }
                }
            }
        }
    }

    // Store component sizes (largest connected land) in a map from "root" -> size
    unordered_map<int, int> compSize;
    for (int r = 0; r < m; r++)
    {
        for (int c = 0; c < n; c++)
        {
            if (grid[r][c] == 1)
            {
                int root = dsu.findp(idx(r, c));
                compSize[root] = dsu.size[root];
            }
        }
    }

    int ans = 0;
    if (!compSize.empty())
    {
        // current largest without filling any water
        for (auto &kv : compSize)
            ans = max(ans, kv.second);
    }

    // For each water cell, sum distinct neighboring components +1
    for (int r = 0; r < m; r++)
    {
        for (int c = 0; c < n; c++)
        {
            if (grid[r][c] == 0)
            {
                unordered_set<int> neighborComps;
                for (auto &d : DIRS)
                {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1)
                    {
                        neighborComps.insert(dsu.findp(idx(nr, nc)));
                    }
                }
                int newIslandSize = 1; // for this filled cell
                for (auto rootID : neighborComps)
                {
                    newIslandSize += compSize[rootID];
                }
                ans = max(ans, newIslandSize);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}