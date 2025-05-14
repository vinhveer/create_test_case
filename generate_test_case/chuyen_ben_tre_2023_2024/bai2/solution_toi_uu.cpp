#include <iostream>
using namespace std;

int main() {
    unsigned int N;
    cin >> N;
    if (N == 0) {
        cout << 0 << '\n';
        return 0;
    }
    string res;
    while (N) {
        res = char('0' + (N & 1)) + res;
        N >>= 1;
    }
    cout << res << '\n';
    return 0;
}