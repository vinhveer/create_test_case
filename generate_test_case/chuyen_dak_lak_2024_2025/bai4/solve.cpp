#include <bits/stdc++.h>
using namespace std;

static const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; long long K;
    cin >> N >> K;
    vector<long long> a(N);
    for(int i=0; i<N; i++){
        cin >> a[i];
    }

    // Prefix sums for fast subarray sum calculation
    vector<long long> prefix(N+1, 0LL);
    for(int i=1; i<=N; i++){
        prefix[i] = prefix[i-1] + a[i-1];
    }

    // Function to check if ALL subarrays of length len have sum <= K
    auto check = [&](int len) {
        long long maxSub = 0;
        // max of subarray sums of length len
        // if for ANY subarray sum of length len > K, then not valid
        for(int i=0; i+len<=N; i++){
            long long s = prefix[i+len] - prefix[i];
            if(s > K) return false;
        }
        return true;
    };

    // Binary search for the largest L
    int l=1, r=N;
    int ans=-1;
    while(l <= r){
        int mid = (l+r)/2;
        if(check(mid)){
            ans = mid;
            l = mid+1;
        } else {
            r = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}