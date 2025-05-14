#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật "trâu" (Brute Force)
  -----------------------------
  Bài 2. Đếm ước

  - Cho n và dãy a[1..n], mỗi a[i] (1 ≤ a[i] ≤ 10^6).
  - Tìm số ước dương lớn nhất của bất kỳ phần tử nào trong dãy.
  - Chỉ cần độ chính xác tuyệt đối, không quan trọng hiệu năng.

  Hướng tiếp cận "trâu":
  1. Tính số ước dương của một số x:
      + Duyệt d từ 1..x, đếm d nếu x % d == 0.
  2. Với mỗi a[i], tính số ước dương bằng thuật trên, so sánh lấy kết quả lớn nhất.

  Độ phức tạp:
  - O(n * M) với M là giá trị a[i] tối đa, n ≤ 10^6 và M ≤ 10^6 => tiềm năng O(10^12) phép toán.
  - Thuật này rất chậm, nhưng đúng đắn, minh họa "trâu".
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    int maxCountDiv = 0;

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    // Thuật trâu: tính số ước từng phần tử
    for(int i = 0; i < n; i++){
        int x = a[i];
        int countDiv = 0;
        for(int d = 1; d <= x; d++){
            if(x % d == 0) countDiv++;
        }
        maxCountDiv = max(maxCountDiv, countDiv);
    }

    cout << maxCountDiv << "\n";
    return 0;
}