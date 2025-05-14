#include <bits/stdc++.h>

using namespace std;

long long BinSearch(long long k, vector<long long> a) {

    long long left = 0, right = a.size() - 1;

    while(left <= right) {

        long long mid = left + (right - left) / 2;
        cout << "mid: " << mid << endl;

        if (a[mid] == k) {

            return mid + 1;

        } else if(a[mid] > k) {

            right = mid - 1;

        } else if(a[mid] < k) {

            left = mid + 1;

        }

    }

    return -1;

}

int main() {

    cin.tie(0); ios_base::sync_with_stdio(false); cout.tie(0);

    long long n, k;

    cin >> n >> k;

    vector<long long> a(n);

    for(long long i = 0; i < n; i++) {

        cin >> a[i];

    }

    sort(a.begin(), a.end());

    cout << BinSearch(k, a) << endl;

    return 0;

}