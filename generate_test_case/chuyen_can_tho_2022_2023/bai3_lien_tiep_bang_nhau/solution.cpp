#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;

    int maxlen = 1;
    for (int i = 0; i < n; ++i) {
        int len = 1;
        for (int j = i + 1; j < n; ++j) {
            if (a[j] == a[i]) ++len;
            else break;
        }
        if (len > maxlen) maxlen = len;
    }
    cout << maxlen << endl;
    return 0;
}