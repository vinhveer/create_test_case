#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> x, pair<int, int> y) {
    return x.second < y.second;
}

int main() {
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    // #endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, k;
    cin >> n >> m >> k;

    vector<pair<int, int>> points(k * 4);
    for (int i = 0; i < k * 4; ++i)
        cin >> points[i].first >> points[i].second;

    sort(points.begin(), points.end());
    int diff_x = points[k * 2].first - points[k * 2 - 1].first;

    sort(points.begin(), points.begin() + k * 2, cmp);
    sort(points.begin() + k * 2, points.end(), cmp);

    int diff_y = max(0,
        min(points[k].second, points[k * 3].second)
        - max(points[k - 1].second, points[k * 3 - 1].second)
    );

    cout << 1LL * diff_x * diff_y << '\n';

    return 0;
}
