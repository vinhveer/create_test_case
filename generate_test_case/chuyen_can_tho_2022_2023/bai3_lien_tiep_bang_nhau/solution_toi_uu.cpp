#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int prev, curr, len = 1, maxlen = 1;
    cin >> prev;
    for (int i = 1; i < n; ++i) {
        cin >> curr;
        if (curr == prev) ++len;
        else len = 1;
        if (len > maxlen) maxlen = len;
        prev = curr;
    }
    cout << maxlen << '\n';
    return 0;
}