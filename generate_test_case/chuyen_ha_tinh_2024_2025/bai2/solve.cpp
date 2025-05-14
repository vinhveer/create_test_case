#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật Tối Ưu - Bài 2. Đếm ước
  -----------------------------
  - Mục tiêu: Tím số ước dương lớn nhất của bất kỳ a[i].
  - Ràng buộc: n ≤ 10^6, a[i] ≤ 10^6.
  -------------------------------------
  Cách giải:
    1. Tìm maxVal = max(a[i]) cho i=1..n.
    2. Tạo mảng divisorCount[maxVal+1], ban đầu = 0.
    3. Duyệt i từ 1..maxVal:
       for j in [i..maxVal..i]:
          divisorCount[j]++   // i là ước của j
    4. Tìm maxCount = max(divisorCount[a[i]]) với i=1..n.
    5. In maxCount.

  Độ phức tạp:
    - Bước 3: O(maxVal * (maxVal / i)) ~ O(maxVal log(maxVal)) 
    - Với maxVal ≤ 10^6, có thể thực thi kịp ở C++.

  Đảm bảo kết quả đúng, tối ưu so với thuật trâu O(n * maxVal).
*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> arr(n);
    int maxVal = 0;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
        if(arr[i] > maxVal) maxVal = arr[i];
    }

    vector<int> divisorCount(maxVal + 1, 0);

    // Tính số ước cho mọi giá trị đến maxVal
    for(int i = 1; i <= maxVal; i++){
        for(int j = i; j <= maxVal; j += i){
            divisorCount[j]++;
        }
    }

    int ans = 0;
    for(int x : arr){
        ans = max(ans, divisorCount[x]);
    }

    cout << ans << "\n";
    return 0;
}