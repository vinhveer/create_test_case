#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật "trâu" (Brute Force)
  -----------------------------
  Bài 5:
    - Cho N, và dãy a[1..N].
    - c(x) = số bộ ba chỉ số (i, j, k) thỏa mãn:
          1 ≤ i < j < k < x
          a_i + a_j + a_k = a_x
    - N ≤ 5000.

  Ý tưởng "trâu":
    - Với mỗi x từ 1..N:
      + Duyệt tất cả i, j, k < x thứ tự i < j < k.
      + Kiểm tra a_i + a_j + a_k == a_x.
      + Đếm số lần thỏa mãn.
    - Thời gian O(N^4) theo lý thuyết, nhưng "độ trâu" nhấn mạnh tính đúng đắn,
      không ưu tiên hiệu suất.

  Chú ý:
    - Dữ liệu vào: N (1 ≤ N ≤ 5000), a[i] (|a[i]| ≤ 10^6).
    - Xuất N số c(1), c(2), ..., c(N).

  Để tránh tràn số khi cộng a_i + a_j + a_k:
    - Mỗi a[i] ≤ 10^6, tổng tối đa 3*10^6, vừa trong kiểu 32-bit
      (nhưng ta vẫn dùng 64-bit khi cần).

  Độ phức tạp:
    - Thuần brute force: O(N^4) (rất chậm), nhưng đảm bảo đúng.
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> a(N+1);
    for(int i = 1; i <= N; i++){
        cin >> a[i];
    }

    // Kết quả c(x) cho x = 1..N
    vector<long long> c(N+1, 0LL);

    // Tính c(x) brute force
    // for x in [1..N] => for i<j<k<x => if a_i+a_j+a_k == a_x => c(x)++
    for(int x = 1; x <= N; x++){
        long long count_x = 0;
        for(int i = 1; i < x - 1; i++){
            for(int j = i + 1; j < x; j++){
                for(int k = j + 1; k < x; k++){
                    if(a[i] + a[j] + a[k] == a[x]){
                        count_x++;
                    }
                }
            }
        }
        c[x] = count_x;
    }

    // Xuất kết quả
    for(int x = 1; x <= N; x++){
        cout << c[x];
        if(x < N) cout << " ";
    }
    cout << "\n";

    return 0;
}