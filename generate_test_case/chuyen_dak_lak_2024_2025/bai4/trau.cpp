#include <bits/stdc++.h>
using namespace std;

/*
  ----- Thuật "trâu" (Brute Force) -----
  Yêu cầu độ chính xác cao, không cần nhanh.

  Ý tưởng:
   - Đọc N, K và mảng a.
   - Tạo mảng prefixSum để tính tổng tiền tố, prefixSum[0] = 0, prefixSum[i] = prefixSum[i-1] + a[i].
   - Duyệt L từ N giảm xuống 1:
     + Xét tất cả các dãy con liên tiếp độ dài L:
       * Tính tổng bằng prefixSum[j+L-1] - prefixSum[j-1].
       * Nếu bất kỳ dãy con nào có tổng > K thì L không thỏa mãn.
     + Nếu duyệt hết và tổng mọi dãy con liên tiếp đều ≤ K, in ra L và kết thúc.
   - Nếu không tìm được L nào thỏa mãn, in -1.

  Độ phức tạp:
   - O(N^2) ở trường hợp xấu nhất (về lý thuyết),
     do việc kiểm tra từng độ dài L và quét các dãy con liên tiếp.
   - Đáp ứng đúng yêu cầu "trâu": đảm bảo chính xác, không quan trọng tốc độ.
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, K;
    cin >> N >> K;
    vector<long long> a(N + 1, 0LL);
    for(int i = 1; i <= N; i++) {
        cin >> a[i];
    }

    // Tạo prefix sum
    vector<long long> prefixSum(N+1, 0LL);
    for(int i = 1; i <= N; i++){
        prefixSum[i] = prefixSum[i-1] + a[i];
    }

    // Tiến hành duyệt L từ lớn xuống bé
    for(int L = N; L >= 1; L--){
        bool valid = true;
        for(int start = 1; start + L - 1 <= N; start++){
            long long subSum = prefixSum[start + L - 1] - prefixSum[start - 1];
            if(subSum > K){
                valid = false;
                break;
            }
        }
        if(valid){
            cout << L << "\n";
            return 0;
        }
    }

    // Nếu không có L nào thỏa mãn
    cout << -1 << "\n";
    return 0;
}