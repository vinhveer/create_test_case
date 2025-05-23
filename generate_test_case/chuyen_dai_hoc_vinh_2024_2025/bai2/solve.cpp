#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    // Check if n is within constraints
    if (n < 1 || n > 5 * 10000) {
        cout << -1 << endl;
        return 0;
    }
    
    // Read the first sequence
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    // Read the second sequence
    vector<int> b(n);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    
    // Check if the sequences are corresponding
    unordered_map<int, int> a_to_b;
    unordered_map<int, int> b_to_a;
    bool isCorresponding = true;
    
    for (int i = 0; i < n; i++) {
        // Check condition: if a_i = a_j then b_i = b_j
        auto it_a = a_to_b.find(a[i]);
        if (it_a != a_to_b.end()) {
            if (it_a->second != b[i]) {
                isCorresponding = false;
                break;
            }
        } else {
            a_to_b[a[i]] = b[i];
        }
        
        // Check condition: if a_i ≠ a_j then b_i ≠ b_j
        // This is equivalent to checking: if b_i = b_j then a_i = a_j
        auto it_b = b_to_a.find(b[i]);
        if (it_b != b_to_a.end()) {
            if (it_b->second != a[i]) {
                isCorresponding = false;
                break;
            }
        } else {
            b_to_a[b[i]] = a[i];
        }
    }
    
    if (isCorresponding) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
    
    return 0;
}
