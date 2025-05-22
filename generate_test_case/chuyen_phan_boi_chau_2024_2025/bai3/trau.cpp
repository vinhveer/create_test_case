#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
using ll = long long;
const int MOD = 1e9+7;

// Đếm số mũ của p trong n!
ll count_p(ll n, ll p) {
    ll res = 0;
    for (ll div = p; div <= n; div *= p)
        res += n / div;
    return res;
}

// Đếm số mũ của p trong a! / (b!)
// (tức là số mũ p trong a! - số mũ p trong b!)
ll count_p_range(ll a, ll b, ll p) {
    return count_p(b, p) - count_p(a-1, p);
}

// THUẬT TRÂU: Nếu b-a nhỏ, tính tích thực sự và đếm số 0 tận cùng
int count_zero_brute(ll a, ll b) {
    ll prod = 1;
    for (ll i = a; i <= b; ++i)
        prod *= i;
    int cnt = 0;
    while (prod % 10 == 0) {
        ++cnt;
        prod /= 10;
    }
    return cnt;
}

int main() {
    int T;
    cin >> T;
    vector<ll> res(T);
    for (int t = 0; t < T; ++t) {
        ll a, b;
        cin >> a >> b;
        // Nếu b-a nhỏ, dùng thuật trâu chuẩn
        if (b - a <= 18 && b <= 100000000000000000LL) {
            res[t] = count_zero_brute(a, b) % MOD;
        } else {
            // Đếm số mũ của 2 và 5 trong dãy a..b
            ll twos = 0, fives = 0;
            // Số mũ của p trong a..b = sum_{i=a}^b (số mũ p trong i)
            // = count_p(b, p) - count_p(a-1, p)
            twos = count_p(b, 2) - count_p(a-1, 2);
            fives = count_p(b, 5) - count_p(a-1, 5);
            res[t] = min(twos, fives) % MOD;
        }
    }
    for (int t = 0; t < T; ++t)
        cout << res[t] << '\n';
    return 0;
}