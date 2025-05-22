#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Thuật toán trâu: Thử mọi khả năng về độ dài S, kiểm tra đúng cấu trúc T = S + K
int main() {
    string T;
    char ch;
    cin >> T >> ch;
    int L = T.length();

    // Sẽ thử mọi độ dài S từ 1 đến L-1
    for (int lenS = 1; lenS < L; ++lenS) {
        string S = T.substr(0, lenS);
        // sinh K từ S bằng loại bỏ tất cả ký tự ch
        string K;
        for (char c : S) if (c != ch) K += c;
        // T = S + K ?
        if ((int)(S.length() + K.length()) != L) continue; // tổng độ dài phải đúng
        if (T.substr(lenS) == K) {
            cout << S << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}