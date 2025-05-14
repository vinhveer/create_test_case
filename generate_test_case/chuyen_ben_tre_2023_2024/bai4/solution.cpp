#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;
    int res = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (i != j) {
                int prodA = a[i] * a[j];
                int prodB = b[i] * b[j];
                res = max(res, min(prodA, prodB));
            }
    cout << res << endl;
    return 0;
}