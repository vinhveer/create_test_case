#include <iostream>
#include <vector>
using namespace std;

// Hàm kiểm tra số nguyên tố
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // Kiểm tra các số từ 5 đến căn bậc 2 của n
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// Hàm tính tổng các chữ số
int sumOfDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// Hàm đếm số song nguyên tố trong đoạn [L, R]
int countSongNguyenTo(int L, int R) {
    // Kiểm tra ràng buộc đầu vào
    if (!(1 < L && L <= R && R <= 1000000)) {
        return -1;
    }
    
    int count = 0;
    // Duyệt qua từng số trong đoạn [L, R]
    for (int i = L; i <= R; i++) {
        // Kiểm tra nếu i là số nguyên tố
        if (isPrime(i)) {
            // Tính tổng các chữ số của i
            int digitSum = sumOfDigits(i);
            // Kiểm tra nếu tổng các chữ số cũng là số nguyên tố
            if (isPrime(digitSum)) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    int L, R;
    cin >> L >> R;
    
    int result = countSongNguyenTo(L, R);
    cout << result << endl;
    
    return 0;
}