#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int n;
    cin >> n;
    vector<ll> A(n + 1);
    for(int i = 1; i <= n; i++) {
        cin >> A[i];
    }
    
    ll minCost = LLONG_MAX;
    
    // Thử mỗi vị trí x từ 2 đến n-1 làm đỉnh núi
    for(int x = 2; x <= n - 1; x++) {
        // Tìm giá trị tối thiểu mà đỉnh x cần đạt để thỏa mãn tăng chặt bên trái
        ll leftPeak = A[1];
        for(int i = 2; i <= x; i++) {
            leftPeak = max(leftPeak + 1, A[i]);
        }
        
        // Tìm giá trị tối thiểu mà đỉnh x cần đạt để thỏa mãn giảm chặt bên phải
        ll rightPeak = A[n];
        for(int i = n - 1; i >= x; i--) {
            rightPeak = max(rightPeak + 1, A[i]);
        }
        
        // Giá trị đỉnh x phải là max của leftPeak và rightPeak
        ll minPeak = max(leftPeak, rightPeak);
        
        // Thử mọi giá trị peak từ minPeak trở lên
        // Giới hạn trên có thể là một số rất lớn, ở đây chọn 10^9 + n để đảm bảo đủ
        for(ll peak = minPeak; peak <= minPeak + n; peak++) {
            vector<ll> B = A; // Sao chép mảng gốc
            ll cost = 0;
            
            // Điều chỉnh phần bên trái thành dãy tăng chặt
            B[x] = peak;
            cost += max(0LL, peak - A[x]);
            for(int i = x - 1; i >= 1; i--) {
                if(B[i] >= B[i + 1]) {
                    B[i] = B[i + 1] - 1;
                    cost += max(0LL, A[i] - B[i]);
                } else if(B[i] < B[i + 1] - 1) {
                    B[i] = B[i + 1] - 1;
                    cost += max(0LL, B[i] - A[i]);
                }
            }
            
            // Điều chỉnh phần bên phải thành dãy giảm chặt
            for(int i = x + 1; i <= n; i++) {
                if(B[i] >= B[i - 1]) {
                    B[i] = B[i - 1] - 1;
                    cost += max(0LL, A[i] - B[i]);
                } else if(B[i] < B[i - 1] - 1) {
                    B[i] = B[i - 1] - 1;
                    cost += max(0LL, B[i] - A[i]);
                }
            }
            
            // Kiểm tra xem mảng B đã là ngọn núi hợp lệ chưa
            bool valid = true;
            for(int i = 1; i < x; i++) {
                if(B[i] >= B[i + 1]) {
                    valid = false;
                    break;
                }
            }
            for(int i = x; i < n; i++) {
                if(B[i] <= B[i + 1]) {
                    valid = false;
                    break;
                }
            }
            
            if(valid) {
                minCost = min(minCost, cost);
            }
        }
    }
    
    cout << minCost << endl;
    return 0;
}