#include <bits/stdc++.h>
using namespace std;

/*
  Bài: Đếm số lượng số nguyên dương là bội của 3 hoặc 5 trong phạm vi từ 1 đến N

  Yêu cầu:
    - Đọc T (1 ≤ T ≤ 100) bộ dữ liệu.
    - Mỗi bộ dữ liệu có 1 giá trị N (1 ≤ N ≤ 10^10).
    - Đếm có bao nhiêu số trong [1..N] là bội của 3 hoặc bội của 5.

  Ý tưởng chính: Nguyên tắc bao hàm - loại trừ
    Số bội 3 hoặc 5 = số bội 3 + số bội 5 - số bội 15.

  Các trường hợp có thể thiếu:
    - N = 1, 2 (nhỏ hơn 3, không có bội 3 hoặc 5 -> kết quả = 0).
    - N lớn (lên đến 10^10).
  
  Thuật giải quen thuộc:
    count = floor(N / 3) + floor(N / 5) - floor(N / 15).
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        long long N;
        cin >> N;
        // Tính các bội 3, 5, 15
        long long multiplesOf3 = N / 3;
        long long multiplesOf5 = N / 5;
        long long multiplesOf15 = N / 15;

        long long result = multiplesOf3 + multiplesOf5 - multiplesOf15;
        cout << result << "\n";
    }
    return 0;
}