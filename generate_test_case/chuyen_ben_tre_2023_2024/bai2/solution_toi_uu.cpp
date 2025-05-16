#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long x) {
    if (x < 2) return false;
    if (x % 2 == 0) return (x == 2);
    for (long long i = 3; i * i <= x; i += 2) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int countPrimeSolutions = 0;
    while (N--) {
        long long a, b;
        cin >> a >> b;
        // ax + b = 0 => x = -b / a
        if (-b % a == 0) {
            long long x = -b / a;
            if (x > 0 && isPrime(x)) {
                countPrimeSolutions++;
            }
        }
    }
    cout << countPrimeSolutions << "\n";
    return 0;
}