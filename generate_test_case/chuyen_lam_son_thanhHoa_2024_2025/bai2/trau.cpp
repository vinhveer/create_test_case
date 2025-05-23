#include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra số nguyên tố
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true; 
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

// Hàm đếm số ước của một số (thuật trâu, độ phức tạp O(√n))
int countDivisors(int n) {
    int countDiv = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            if (i * i == n) countDiv += 1; 
            else countDiv += 2;
        }
    }
    return countDiv;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    cin >> T;
    while (T--) {
        int a, b;
        cin >> a >> b;
        long long result = 0;
        // Đảm bảo a <= b
        if (a > b) {
            cout << 0 << "\n";
            continue;
        }
        // Kỹ thuật đếm trâu
        for (int num = a; num <= b; num++) {
            int divC = countDivisors(num);
            if (isPrime(divC)) {
                result++;
            }
        }
        cout << result << "\n";
    }

    return 0;
}