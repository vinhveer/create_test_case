#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật "trâu" (Brute Force)
  -----------------------------
  Bài 3. Tổng chẵn

  - Cho n và dãy a[1..n], mỗi a[i] (0 ≤ a[i] ≤ 10^6).
  - Đếm số cặp (i, j), i < j, sao cho (tổng các phần tử còn lại) là số chẵn.
  - (i, j) và (j, i) được tính là 1 cách, nên chỉ cần duyệt i < j.

  Ý tưởng "trâu":
    1. Tính S = tổng của toàn bộ dãy.
    2. Với mỗi cặp (i, j):
       - sum_after_remove = S - a[i] - a[j].
       - sum_after_remove % 2 == 0 => đếm vào kết quả.
    3. Kết quả thu được sau O(n^2).

  Độ phức tạp:
    - O(n^2), có thể quá lớn cho n = 10^6, nhưng yêu cầu "trâu" thì được chấp nhận để minh họa.
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    long long S = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        S += a[i];
    }

    long long countPairs = 0;
    // Duyệt i < j
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            long long sumAfter = S - a[i] - a[j];
            if(sumAfter % 2 == 0){
                countPairs++;
            }
        }
    }

    cout << countPairs << "\n";
    return 0;
}