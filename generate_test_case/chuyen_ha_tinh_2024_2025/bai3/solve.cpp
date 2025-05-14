#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật Tối Ưu - Bài 3. Tổng chẵn
  -----------------------------

  - Cho n (2 ≤ n ≤ 10^6), và dãy a[1..n], mỗi a[i] (0 ≤ a[i] ≤ 10^6).
  - Đếm số cặp (i, j) (i < j) để sau khi xóa a[i], a[j], tổng còn lại chẵn.

  Phân tích:
  - Sum = tổng dãy ban đầu.
  - sum_after_remove = Sum - a[i] - a[j].
  - sum_after_remove % 2 = 0 --> (Sum - a[i] - a[j]) % 2 = 0
    --> Sum % 2 = (a[i] + a[j]) % 2.

  Ghi chú:
  - (x + y) % 2 = 0 => x và y cùng chẵn hoặc cùng lẻ.
  - (x + y) % 2 = 1 => x và y một chẵn một lẻ.

  => Nếu Sum chẵn, ta cần cặp (a[i], a[j]) có tổng chẵn => cùng parity.
     Nếu Sum lẻ, ta cần cặp (a[i], a[j]) có tổng lẻ => khác parity.

  Thuật toán O(n):
    1) Tính Sum mod 2.
    2) Đếm số phần tử chẵn (cntEven) và lẻ (cntOdd).
    3) Nếu sum mod 2 == 0:
         - Số cặp (chẵn, chẵn) = cntEven * (cntEven - 1) / 2
         - Số cặp (lẻ, lẻ) = cntOdd * (cntOdd - 1) / 2
         => Kết quả = tổng hai giá trị trên
       Nếu sum mod 2 == 1:
         - Số cặp (chẵn, lẻ) = cntEven * cntOdd
         => Kết quả

  Độ phức tạp:
    - O(n) duyệt mảng, O(1) tính toán còn lại.
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    long long sumAll = 0;
    long long cntEven = 0, cntOdd = 0;

    for(int i = 0; i < n; i++){
        cin >> a[i];
        sumAll += a[i];
    }

    for(int i = 0; i < n; i++){
        if(a[i] % 2 == 0) cntEven++;
        else cntOdd++;
    }

    long long ans = 0;
    if((sumAll % 2) == 0) {
        // Sum chẵn => (a[i] + a[j]) cần chẵn => cùng parity
        ans = cntEven * (cntEven - 1) / 2 + cntOdd * (cntOdd - 1) / 2;
    } else {
        // Sum lẻ => (a[i] + a[j]) cần lẻ => khác parity
        ans = cntEven * cntOdd;
    }

    cout << ans << "\n";
    return 0;
}