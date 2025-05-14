#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    // Số chia hết cho 2 và 3 là bội của 6
    int first = (a + 5) / 6 * 6;
    int last = (b / 6) * 6;
    if (first > b) {
        cout << 0 << endl;
        return 0;
    }
    int n = (last - first) / 6 + 1;
    long long sum = 1LL * n * (first + last) / 2;
    cout << sum << endl;
    return 0;
}