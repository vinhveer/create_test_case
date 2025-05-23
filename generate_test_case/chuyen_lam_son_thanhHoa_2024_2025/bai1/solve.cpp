#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long L, R;
    cin >> L >> R;
    
    // Adjust L to the first even number >= L
    if (L % 2 != 0)
        L++;
    
    // Adjust R to the last even number <= R
    if (R % 2 != 0)
        R--;
    
    // If there are no even numbers in the range
    if (L > R) {
        cout << 0 << "\n";
        return 0;
    }
    
    // Calculate the count of even numbers in the range
    long long count = (R - L) / 2 + 1;
    
    // Use arithmetic progression formula: sum = (first + last) * count / 2
    long long sum = (L + R) * count / 2;
    
    cout << sum << "\n";
    
    return 0;
}