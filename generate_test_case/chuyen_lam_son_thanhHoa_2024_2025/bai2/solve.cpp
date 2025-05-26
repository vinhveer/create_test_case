#include <bits/stdc++.h>
using namespace std;

// Precompute the smallest prime factor (spf) for each number up to MAXN.
// Then use it to quickly find the divisor count of each number.
// Finally, use a prefix-sum array to answer each query in O(1).

static const int MAXN = 1000000; // Up to 10^6, per the problem statement

// Build the sieve for smallest prime factor in O(n log log n).
// spf[x] will store the smallest prime divisor of x.
vector<int> buildSPF(int n) {
    vector<int> spf(n+1, 0);
    spf[1] = 1;
    for (int i = 2; i <= n; i++) {
        if (spf[i] == 0) { 
            // i is prime
            spf[i] = i;
            if ((long long)i * i <= n) {
                for (int j = i * i; j <= n; j += i) {
                    if (spf[j] == 0) {
                        spf[j] = i;
                    }
                }
            }
        }
    }
    return spf;
}

// Compute the number of divisors using the smallest prime factor array.
// If n = p1^e1 * p2^e2 * ... then #divisors = (e1+1)*(e2+1)*...
int divisorCount(int x, const vector<int> &spf) {
    int total = 1;
    while (x > 1) {
        int primeFactor = spf[x];
        int expCount = 0;
        while (spf[x] == primeFactor) {
            x /= primeFactor;
            expCount++;
        }
        total *= (expCount + 1);
    }
    return total;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // Precompute spf for all numbers up to MAXN
    vector<int> spf = buildSPF(MAXN);

    // Precompute all divisor counts
    vector<int> divCount(MAXN+1, 0);
    for (int i = 1; i <= MAXN; i++){
        divCount[i] = divisorCount(i, spf);
    }

    // We only need to know if a divisor count is prime up to around 240~1000
    // because that's usually the upper bound for # of divisors for numbers <= 1e6.
    // To be safe, let's handle up to 1000.
    static const int MAX_DC = 1000;
    vector<bool> isPrimeDC(MAX_DC+1, true);
    isPrimeDC[0] = false;
    isPrimeDC[1] = false;
    for(int i = 2; i * i <= MAX_DC; i++){
        if(isPrimeDC[i]){
            for(int j = i*i; j <= MAX_DC; j += i){
                isPrimeDC[j] = false;
            }
        }
    }

    // Build a prefix sum array where pref[i] = number of valid numbers up to i
    // (valid meaning that the number of divisors is prime)
    vector<int> pref(MAXN+1, 0);
    for(int i = 1; i <= MAXN; i++){
        pref[i] = pref[i-1] + (isPrimeDC[ divCount[i] ] ? 1 : 0);
    }

    // Process queries
    int T; cin >> T;
    while(T--){
        int a, b;
        cin >> a >> b;
        if(a < 1) a = 1; 
        if(b > MAXN) b = MAXN; // Problem states up to 1e6, but just a safe check.

        if(a > b){
            cout << 0 << "\n";
            continue;
        }
        cout << (pref[b] - pref[a-1]) << "\n";
    }

    return 0;
}
