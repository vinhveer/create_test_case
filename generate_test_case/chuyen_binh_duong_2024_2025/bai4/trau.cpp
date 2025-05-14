// Thuật trâu: sinh tất cả hoán vị của mảng B, kiểm tra điều kiện đề bài
// Đúng tuyệt đối, chỉ dùng cho N <= 8~9

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) A[i] = i+1;
    vector<int> B = A;
    bool found = false;
    do {
        bool ok = true;
        for (int i = 0; i < N; ++i) {
            if (abs(B[i] - A[i]) != K) {
                ok = false;
                break;
            }
        }
        if (ok) {
            found = true;
            for (int i = 0; i < N; ++i) cout << B[i] << (i == N-1 ? "\n" : " ");
            // Không return, vì đề bài có thể muốn in ra tất cả các hoán vị thỏa mãn
        }
    } while (next_permutation(B.begin(), B.end()));
    if (!found) cout << -1 << endl;
    return 0;
}