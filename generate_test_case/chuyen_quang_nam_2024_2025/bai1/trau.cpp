#include <bits/stdc++.h>
using namespace std;

// Sinh dãy Fibonacci nhỏ hơn hoặc bằng 1e9
vector<int> generate_fibo() {
    vector<int> fibo = {1, 1};
    while (true) {
        int nxt = fibo[fibo.size() - 1] + fibo[fibo.size() - 2];
        if (nxt > 1000000000) break;
        fibo.push_back(nxt);
    }
    return fibo;
}

int main() {
    freopen("SUMFIBO.INP", "r", stdin);
    freopen("SUMFIBO.OUT", "w", stdout);

    int N;
    cin >> N;

    vector<int> fibo = generate_fibo();
    vector<int> res;

    // Tham lam ngược: chọn số Fibonacci lớn nhất <= N, trừ đi, lặp lại
    for (int i = fibo.size() - 1; i >= 0; --i) {
        if (fibo[i] <= N) {
            res.push_back(fibo[i]);
            N -= fibo[i];
        }
    }

    // In ra theo thứ tự lớn đến bé
    for (int i = 0; i < res.size(); ++i) {
        if (i) cout << " ";
        cout << res[i];
    }
    cout << "\n";
    return 0;
}