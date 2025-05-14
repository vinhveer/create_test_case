#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Read input
    int n;
    cin >> n;
    vector<long long> a(n+1);
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    int m;
    cin >> m;
    vector<long long> b(m+1);
    for(int j = 1; j <= m; j++) {
        cin >> b[j];
    }

    // canUseA[i] = true if the prefix a[1..i] is non-decreasing
    vector<bool> canUseA(n+1, true);
    for(int i = 2; i <= n; i++){
        if(a[i] < a[i-1]) {
            canUseA[i] = false;
        }
    }
    // We'll fix it so canUseA[i] means "a[1..i] is entirely non-decreasing"
    // This means canUseA[i] = canUseA[i-1] && (a[i] >= a[i-1])
    for(int i = 2; i <= n; i++){
        canUseA[i] = canUseA[i] && canUseA[i-1];
    }

    // canUseB[j] = true if the suffix b[j..m] is non-decreasing
    vector<bool> canUseB(m+2, true);
    for(int j = m-1; j >= 1; j--){
        if(b[j] > b[j+1]) {
            canUseB[j] = false;
        }
    }
    // Similarly, canUseB[j] = canUseB[j+1] && (b[j] <= b[j+1])
    for(int j = m-1; j >= 1; j--){
        canUseB[j] = canUseB[j] && canUseB[j+1];
    }

    long long ans = 0;

    // Brute force: Try all prefixes i and suffixes j
    // Check if a[1..i] is non-decreasing, b[j..m] is non-decreasing,
    // and a[i] <= b[j]. Keep track of the maximum i + (m-j+1).
    for(int i = 1; i <= n; i++){
        if(!canUseA[i]) continue; // prefix a[1..i] isn't non-decreasing
        for(int j = 1; j <= m; j++){
            if(!canUseB[j]) continue; // suffix b[j..m] isn't non-decreasing
            if(a[i] <= b[j]) {
                long long length = (long long)i + (long long)(m - j + 1);
                ans = max(ans, length);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}