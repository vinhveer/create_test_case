#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật "trâu" (Brute Force)
  -----------------------------
  Bài 4. Đặt trạm phát sóng

  - Cho n điểm dân cư (x_i, y_i) và bán kính phủ sóng k.
  - Mục tiêu: Đặt trạm tại một vị trí p (đã được đánh dấu) sao cho 
    số người trong vùng [p-k, p+k] đạt tối đa.
  - Dữ liệu có thể rất lớn (n đến 10^6, x_i đến 10^9), 
    nhưng ta minh họa cách làm "thô", không quan tâm tốc độ:
    1. Đọc n, k và dãy (x_i, y_i).
    2. Tìm minX = min(x_i), maxX = max(x_i).
    3. Xét mọi vị trí p từ 0..maxX (hoặc lớn hơn nếu cần),
       tính tổng y_i của những x_i trong khoảng [p - k, p + k].
       Cập nhật kết quả lớn nhất.
  - Độ phức tạp: O((maxX+1) * n), cực kỳ lớn, 
    nhưng đảm bảo đúng đáp án (nếu thực thi được).
*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    cin >> n >> k;
    vector<long long> x(n), y(n);

    long long minX = LLONG_MAX, maxX = 0;
    for(int i = 0; i < n; i++){
        cin >> x[i] >> y[i];
        if(x[i] < minX) minX = x[i];
        if(x[i] > maxX) maxX = x[i];
    }

    long long best = 0;
    // Brute force vị trí p từ 0 đến maxX
    // (Tuỳ chỉnh nếu muốn xét cả <0, nhưng đề bài ví dụ thường >=0)
    for(long long p = 0; p <= maxX; p++){
        long long coverageMin = p - k;
        long long coverageMax = p + k;
        long long sumPeople = 0;
        for(int i = 0; i < n; i++){
            if(x[i] >= coverageMin && x[i] <= coverageMax){
                sumPeople += y[i];
            }
        }
        best = max(best, sumPeople);
    }

    cout << best << "\n";
    return 0;
}