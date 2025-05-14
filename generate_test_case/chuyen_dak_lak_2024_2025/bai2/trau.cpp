// Thuật trâu: Xét từng phương trình, tìm nghiệm nguyên x = -b/a (a != 0), kiểm tra x > 0 và x là số nguyên tố
// Kiểm tra nguyên tố bằng cách thử tất cả ước từ 2 đến sqrt(x) (x nhỏ nhất là 2, lớn nhất có thể tới 10^12 + 10^12 = 2*10^12)

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Kiểm tra số nguyên tố (brute force cho x <= 2e12, nhưng N <= 20 nên ổn)
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
    int count = 0;
    for (int i = 0; i < N; ++i) {
        long long a, b;
        cin >> a >> b;
        // Điều kiện nghiệm nguyên: -b % a == 0
        if (a == 0) continue;
        if ((-b) % a != 0) continue;
        long long x = (-b) / a;
        if (x > 0 && is_prime(x)) count++;
    }
    cout << count << endl;
    return 0;
}