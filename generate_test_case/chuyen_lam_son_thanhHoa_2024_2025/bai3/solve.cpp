#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// Inline function for GCD using iterative approach
inline ll gcd(ll a, ll b) {
    while (b) {
        ll t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while (T--) {
        ll a, b, N;
        cin >> a >> b >> N;
        
        // Special case: a = b
        if (a == b) {
            cout << a * N << "\n";
            continue;
        }
        
        // Ensure a is smaller than b for simplicity
        if (a > b) {
            swap(a, b);
        }
        
        // Calculate LCM once
        ll g = gcd(a, b);
        ll lcm_val = (a / g) * b; // Avoiding potential overflow
        
        // Binary search with a tighter upper bound
        // The Nth multiple cannot exceed N * a
        ll left = 1;
        ll right = min(N * a, (ll)2e18); // Use a reasonable constraint
        ll result = 0;
        
        while (left <= right) {
            ll mid = left + (right - left) / 2; // Avoid potential overflow
            
            // Calculate how many numbers in sequence are <= mid
            ll count = (mid / a) + (mid / b) - (mid / lcm_val);
            
            if (count >= N) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        cout << result << "\n";
    }
    
    return 0;
}
