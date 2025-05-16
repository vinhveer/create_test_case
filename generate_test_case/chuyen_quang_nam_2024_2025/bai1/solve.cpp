#include <bits/stdc++.h>
using namespace std;

/*
  THUẬT TỐI ƯU (Dựa trên tính chất "Zeckendorf" – mỗi số N có thể được biểu diễn duy nhất
  dưới dạng tổng các số Fibonacci không kề nhau).

  Phân tích:
  - Ta vẫn tạo danh sách Fibonacci <= 10^9.
  - Dùng chiến lược Greedy: luôn chọn Fibonacci lớn nhất <= N, trừ đi và tiếp tục.
  - Độ phức tạp O(log N) về số lượng Fibonacci cần thiết (vì Fibonacci tăng rất nhanh).

  Tuy nhiên, về bản chất, giải pháp tối ưu cũng rất giống "thuật trâu" ở phía trên
  (vì Greedy giải quyết bài này đảm bảo đúng đắn và hiệu quả).
  Chú thích nhiều hơn để người đọc dễ theo dõi.
*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    cin >> N;

    // Tạo dãy Fibonacci đến khi vượt 10^9
    vector<long long> fib;
    fib.push_back(1);
    fib.push_back(1);
    while(true){
        long long next = fib[fib.size()-1] + fib[fib.size()-2];
        if(next > 1000000000LL) break;
        fib.push_back(next);
    }

    vector<long long> ans;
    for(int i = (int)fib.size() - 1; i >= 0; i--){
        if(fib[i] <= N){
            N -= fib[i];
            ans.push_back(fib[i]);
        }
    }

    // In ra kết quả
    for(int i = 0; i < (int)ans.size(); i++){
        cout << ans[i] << (i + 1 < (int)ans.size() ? ' ' : '\n');
    }
    return 0;
}