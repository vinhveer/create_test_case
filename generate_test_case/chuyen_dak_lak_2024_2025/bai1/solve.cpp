#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        long long N;
        cin >> N;
        long long multiplesOf3 = N / 3;
        long long multiplesOf5 = N / 5;
        long long multiplesOf15 = N / 15;
        cout << (multiplesOf3 + multiplesOf5 - multiplesOf15) << "\n";
    }

    return 0;
}