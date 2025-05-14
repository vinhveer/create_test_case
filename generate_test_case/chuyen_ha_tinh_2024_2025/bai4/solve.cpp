#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật Tối Ưu - Bài 4. Đặt trạm phát sóng
  -----------------------------

  Phân tích:
   - Ta có n điểm (x_i, y_i), bán kính k.
   - Mục tiêu: Chọn 1 vị trí p để tối đa tổng y_i với x_i trong [p-k, p+k].
   - Vấn đề: p có thể lên tới 10^9, n có thể tới 10^6.

  Ý tưởng tối ưu (Two-pointer / sliding window):
   1. Gom dữ liệu (x_i, y_i), sắp xếp theo x_i tăng dần.
   2. Dùng hai con trỏ left, right duyệt dãy x đã sắp xếp:
      - Mở rộng right khi x[right] - x[left] <= 2*k (nghĩa là có một p giữa x[left]+k và x[right]-k).
      - Thu thập tổng y trong khoảng [left..right].
      - Nếu khoảng cách x[right] - x[left] > 2*k, thì di chuyển left để thu hẹp khoảng.
   3. Duy trì giá trị tổng y tối đa.

  Chứng minh:
   - Nếu x[right] - x[left] <= 2*k, ta có thể đặt p = (x[left] + x[right])/2 (có thể làm tròn)
     để bao toàn bộ điểm từ x[left]..x[right].
   - Tối ưu so với duyệt tất cả vị trí p.

  Độ phức tạp: O(n log n) (sắp xếp) + O(n) (two-pointer).
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    cin >> n >> k;

    vector<pair<long long, long long>> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i].first >> arr[i].second; 
    }
    // Sắp xếp theo x
    sort(arr.begin(), arr.end(), [](auto &a, auto &b){return a.first < b.first;});

    long long best = 0;
    long long currentSum = 0;
    int left = 0;

    for(int right = 0; right < n; right++){
        currentSum += arr[right].second;
        while(arr[right].first - arr[left].first > 2LL * k){
            // dời left
            currentSum -= arr[left].second;
            left++;
        }
        best = max(best, currentSum);
    }

    cout << best << "\n";
    return 0;
}