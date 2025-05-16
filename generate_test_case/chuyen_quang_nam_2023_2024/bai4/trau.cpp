#include <bits/stdc++.h>
using namespace std;

// Độ chính xác tuyệt đối, thuật trâu: thử mọi cách gán (n nhỏ), hoặc cho n <= m, sắp xếp d tăng, v tăng rồi gán
// Nhưng theo yêu cầu "trâu", ta sinh tổ hợp n xe trong m xe (chọn n xe), thử mọi hoán vị (chỉ cho n, m nhỏ)

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> d(n), v(m);
    for (int i = 0; i < n; ++i) cin >> d[i];
    for (int i = 0; i < m; ++i) cin >> v[i];

    // Trâu với m <= 8 (chọn n xe, thử mọi hoán vị)
    if (m <= 8 && n <= 8) {
        vector<int> idx(m);
        iota(idx.begin(), idx.end(), 0);
        int min_fuel = INT_MAX;
        vector<int> best_xe;
        do {
            vector<int> chosen(idx.begin(), idx.begin() + n);
            // Thử mọi hoán vị cho khớp d với v
            sort(chosen.begin(), chosen.end());
            do {
                int fuel = 0;
                for (int i = 0; i < n; ++i) {
                    fuel += d[i] * v[chosen[i]];
                }
                if (fuel < min_fuel) {
                    min_fuel = fuel;
                    best_xe = chosen;
                }
            } while (next_permutation(chosen.begin(), chosen.end()));
        } while (next_permutation(idx.begin(), idx.end()));
        cout << min_fuel << "\n";
        // In chỉ số xe (tăng dần theo lượng nhiên liệu tiêu tốn)
        vector<pair<int, int>> xe_nl;
        for (int i = 0; i < n; ++i) {
            xe_nl.push_back({d[i] * v[best_xe[i]], best_xe[i]+1});
        }
        sort(xe_nl.begin(), xe_nl.end());
        for (int i = 0; i < n; ++i) {
            cout << xe_nl[i].second << (i == n-1 ? "\n" : " ");
        }
        return 0;
    }
    // Với trường hợp lớn hơn: tham lam (d tăng, v tăng)
    // Sắp xếp d tăng, v tăng, gán d_i với v_i
    vector<pair<int, int>> ds, vs;
    for (int i = 0; i < n; ++i) ds.push_back({d[i], i});
    for (int i = 0; i < m; ++i) vs.push_back({v[i], i+1});
    sort(ds.begin(), ds.end());
    sort(vs.begin(), vs.end());
    long long total = 0;
    vector<pair<long long, int>> xe_used; // (nhiên liệu tiêu tốn, chỉ số xe)
    for (int i = 0; i < n; ++i) {
        long long fuel = 1LL * ds[i].first * vs[i].first;
        total += fuel;
        xe_used.push_back({fuel, vs[i].second});
    }
    // Sắp xếp theo nhiên liệu tiêu tốn tăng dần
    sort(xe_used.begin(), xe_used.end());
    cout << total << "\n";
    for (int i = 0; i < n; ++i) {
        cout << xe_used[i].second << (i == n-1 ? "\n" : " ");
    }
    return 0;
}