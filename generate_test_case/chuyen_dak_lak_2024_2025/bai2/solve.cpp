/*
Giải thích thuật toán tối ưu:
- Với mỗi phương trình ax+b=0 (a != 0), nghiệm là x = -b/a.
- Nếu -b chia hết cho a, và x > 0, kiểm tra x có phải số nguyên tố hay không.
- Kiểm tra số nguyên tố với x <= 2*10^12 vẫn có thể brute-force do N<=20.

Nếu cần tối ưu hóa kiểm tra nguyên tố cho x rất lớn:
- Nếu x chẵn và x > 2: không phải nguyên tố.
- Kiểm tra các ước lẻ từ 3 đến sqrt(x). sqrt(2e12) ~ 1.4e6. Với N=20 vẫn hợp lý.
*/

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(long long x) {
    if (x < 2) return false;
    if (x == 2) return true;
    if (x % 2 == 0) return false;
    for (long long d = 3; d * d <= x; d += 2) {
        if (x % d == 0) return false;
    }
    return true;
}

int main() {
    int N;
    cin >> N;
    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a == 0) continue;
        if ((-b) % a != 0) continue;
        long long x = (-b) / a;
        if (x > 0 && is_prime(x)) cnt++;
    }
    cout << cnt << endl;
    return 0;
}