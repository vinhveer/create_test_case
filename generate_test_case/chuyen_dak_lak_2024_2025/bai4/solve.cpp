#include <bits/stdc++.h>
using namespace std;

/*
  ----- Thuật tối ưu -----
  Mục tiêu: Tìm L lớn nhất sao cho tất cả các dãy con độ dài L
            đều có tổng ≤ K.

  Phân tích:
   - Ta có thể hiểu bài toán: Tìm L lớn nhất với maxSubarraySum(L) ≤ K,
     trong đó maxSubarraySum(L) là tổng lớn nhất của bất kỳ dãy con
     liên tiếp có độ dài L.
   - Nếu maxSubarraySum(L) ≤ K, thì L là khả thi.
     Nếu maxSubarraySum(L) > K, thì L không khả thi.
   - Ta sử dụng prefix sum để tính tổng đoạn liên tiếp trong O(1).
   - maxSubarraySum(L) được tính bằng cách duyệt hết các đoạn dài L,
     lấy max. Chi phí O(N) cho mỗi L.
   - Dùng binary search trên L (từ 1 đến N) để tìm L lớn nhất khả thi.
   - Độ phức tạp: O(N log N), chấp nhận được cho N ≤ 10^5.

  Cách giải:
   - Đọc N, K, mảng a.
   - Tạo prefixSum[].
   - Hàm check(L):
     + Tìm maxSub = max( prefixSum[i+L-1] - prefixSum[i-1] ), i=1..N-L+1
     + Nếu maxSub <= K => true, ngược lại false.
   - Binary search L: left=1, right=N, trả về Lmax thỏa điều kiện, nếu không
     có L nào hợp lệ thì trả -1.
*/

static const long long INF = 1e15;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, K;
    cin >> N >> K;
    vector<long long> a(N+1, 0);
    for(int i = 1; i <= N; i++){
        cin >> a[i];
    }

    // prefixSum
    vector<long long> prefixSum(N+1, 0);
    for(int i = 1; i <= N; i++){
        prefixSum[i] = prefixSum[i-1] + a[i];
    }

    // check function
    auto check = [&](int L) {
        long long maxSum = 0;
        for(int i = 1; i + L - 1 <= N; i++){
            long long subSum = prefixSum[i+L-1] - prefixSum[i-1];
            if(subSum > maxSum) {
                maxSum = subSum;
            }
            if(maxSum > K) return false;
        }
        return (maxSum <= K);
    };

    // binary search
    long long left = 1, right = N;
    long long ans = -1;
    while(left <= right){
        long long mid = (left + right) / 2;
        if(check(mid)){
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}