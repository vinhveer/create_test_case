#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while (T--) {
        ll a, b, N;
        cin >> a >> b >> N;
        
        // Trường hợp đặc biệt: a = b
        if (a == b) {
            cout << a * N << "\n";
            continue;
        }
        
        vector<ll> sequence;
        
        // Giới hạn số lượng phần tử cần xét
        // Giả sử giá trị lớn nhất có thể là 2^60 (đủ lớn cho bài toán)
        const ll MAX_VAL = (ll)1e18;
        
        // Duyệt qua các bội số của a
        for (ll i = 1; i * a <= MAX_VAL && sequence.size() <= 2*N; i++) {
            sequence.push_back(i * a);
        }
        
        // Duyệt qua các bội số của b
        for (ll i = 1; i * b <= MAX_VAL && sequence.size() <= 2*N; i++) {
            sequence.push_back(i * b);
        }
        
        // Loại bỏ các phần tử trùng lặp
        sort(sequence.begin(), sequence.end());
        sequence.erase(unique(sequence.begin(), sequence.end()), sequence.end());
        
        // Đảm bảo có đủ phần tử
        if (N <= sequence.size()) {
            cout << sequence[N-1] << "\n";
        } else {
            cout << "N quá lớn, không thể tính bằng thuật trâu" << "\n";
        }
    }
    
    return 0;
}