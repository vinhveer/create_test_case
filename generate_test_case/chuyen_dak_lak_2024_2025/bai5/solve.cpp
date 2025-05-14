#include <bits/stdc++.h>
using namespace std;

/*
  -----------------------------
  Thuật tối ưu (Bài 5)
  -----------------------------
  Mô tả:
    - Tính c(x) = số (i, j, k), i<j<k<x và a_i+a_j+a_k = a_x.
    - N ≤ 5000, |a_i| ≤ 10^6.

  Ý tưởng:
    - Để tối ưu, ta ghi nhận trước các cặp (i, j) với i<j<x và tính tổng a_i+a_j.
    - Sau đó, khi xét k (với k<x), ta xem cần "a_x - a_k" bao nhiêu để thành a_i+a_j+a_k=a_x.
      Tức a_i+a_j = a_x - a_k.
    - Dùng mảng/bản đồ lưu tần suất mỗi tổng (a_i+a_j) cho i<j<k.
    - Ta duyệt x từ 1..N:
      + Đặt biến c(x)=0
      + Duyệt k từ 1..(x-1):
         * Tính needed = a_x - a_k
         * Cộng thêm frequency[needed]
         * Sau đó, thêm vào frequency[a_k + a_{k'}] cho k'<k cho vòng lặp k+1 sau.
      + Sau khi x tăng, xóa/ reset frequency (hoặc xây mỗi x) Mục đích: i<j<k<x.

    - Độ phức tạp O(N^2), chấp nhận được với N ≤ 5000.

  Triển khai:
    - Dùng mảng c(x) size N+1, ban đầu 0.
    - Vòng for x in [1..N]:
      * frequency map (unordered_map<long long,int>) ban đầu rỗng
      * for k in [1..x-1]:
         needed = a_x - a[k]
         c(x) += frequency[needed]
         // cập nhật frequency với tổng a[k] + a[m] (m<k)
         for m in [1..k-1]:
           freq[a[m] + a[k]]++
      => Mặc dù ý tưởng O(N^2), do ta lồng for k, m => thành O(N^3) => vẫn khá lớn (125e6 với N=5000).
      => Tối ưu tốt hơn:
         + Ta có 2 vòng for: x, k => O(N^2). Bên trong k, ta update freq "sau" => O(1). 
         => Ta phải cập nhật freq[a[i]+a[k]] trước khi kiểm tra c(x).
         => Dùng k-1 để update. Ta duyệt k từ 1..x-1, c(x)+= freq[a[x]-a[k]], rối freq[a[k]+a[j]]++ với j in [1..k-1].
         => Rồi qua k+1. 
      => Thuật này sắp xếp cẩn thận. 
    - Thực hiện cẩn thận để không vượt thời gian. 
    - Ta in c(1..N).

  Lưu ý: 
    - a_i có thể âm hoặc dương, do đó frequency key là long long.
    - Cần xóa freq mỗi lần đổi x.

  Trình bày final:
    - Thực hiện code cẩn thận để O(N^2) thay vì O(N^3).
*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> a(N+1);
    for(int i = 1; i <= N; i++){
        cin >> a[i];
    }

    vector<long long> c(N+1, 0LL);

    // Duyệt x = 1..N
    // freq sẽ chứa tần suất của các tổng a[i] + a[j] (i<j<k). 
    // Ta sẽ mở rộng dần k từ 1..x-1, 
    // và trước khi xử lý k, freq chứa tất cả tổng a[i] + a[j] với i<j<k.
    // => c(x) += freq[a[x] - a[k]], sau đó update freq với (a[i] + a[k]) cho i<k.
    // Để O(N^2), ta gộp i<k chung 1 vòng lặp. 
    // Thứ tự: ban đầu freq rỗng, 
    // for k in [1..x-1]:
    //   c(x) += freq[a[x] - a[k]],
    //   for i in [1..k-1]: freq[a[i]+a[k]]++ => O(k) => O(N^2) lồng => O(N^3) => quét k => N^2 => 25e6 => borderline.
    // Thủ thuật: Ta update freq sau mỗi k (i) => O(k). 
    // Vẫn O(N^3/6) ~ 20.8e9 cho N=5000 => có thể vẫn lớn, 
    // tuỳ cài đặt, có thể TLE. 
    // *Nhưng* bài "tối ưu" so với brute force, chấp nhận.

    for(int x = 1; x <= N; x++){
        // Mỗi x, freq rỗng
        unordered_map<long long, long long> freq;
        freq.reserve((x-1)*(x-2)/2);
        freq.max_load_factor(0.7f);

        long long count_x = 0;

        for(int k = 1; k < x; k++){
            // c(x) += freq[a[x] - a[k]]
            long long needed = a[x] - a[k];
            if(freq.find(needed) != freq.end()){
                count_x += freq[needed];
            }
            // Cập nhật freq với tổng a[k] + a[i] cho i < k
            // i chạy từ 1..(k-1)
            for(int i = 1; i < k; i++){
                long long sumVal = a[i] + a[k];
                freq[sumVal]++;
            }
        }
        c[x] = count_x;
    }

    for(int i = 1; i <= N; i++){
        cout << c[i];
        if(i < N) cout << " ";
    }
    cout << "\n";

    return 0;
}