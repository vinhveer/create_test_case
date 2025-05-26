#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // Read input
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int m;
    cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    
    int max_length = 0;
    
    // Try all possible prefixes of array a
    for (int i = 0; i <= n; i++) {
        bool prefix_valid = true;
        
        // Check if the prefix of a is non-decreasing
        for (int k = 1; k < i; k++) {
            if (a[k] < a[k-1]) {
                prefix_valid = false;
                break;
            }
        }
        
        // If the prefix is not valid, skip this iteration
        if (!prefix_valid && i > 0) {
            continue;
        }
        
        // Try all possible suffixes of array b
        for (int j = 0; j <= m; j++) {
            bool suffix_valid = true;
            
            // Check if the suffix of b is non-decreasing
            for (int k = m-j+1; k < m; k++) {
                if (b[k] < b[k-1]) {
                    suffix_valid = false;
                    break;
                }
            }
            
            // If the suffix is not valid, skip this iteration
            if (!suffix_valid && j > 0) {
                continue;
            }
            
            // Check if the connection between a and b is valid
            bool connection_valid = true;
            if (i > 0 && j > 0 && a[i-1] > b[m-j]) {
                connection_valid = false;
            }
            
            // If all conditions are met, update the maximum length
            if (prefix_valid && suffix_valid && connection_valid) {
                max_length = max(max_length, i + j);
            }
        }
    }
    
    cout << max_length << endl;
    return 0;
}