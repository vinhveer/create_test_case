#include <iostream>
#include <vector>
using namespace std;

int main() {
    unsigned int N;
    cin >> N;
    if (N == 0) {
        cout << 0 << endl;
        return 0;
    }
    vector<int> bits;
    while (N > 0) {
        bits.push_back(N % 2);
        N /= 2;
    }
    for (int i = bits.size() - 1; i >= 0; --i) {
        cout << bits[i];
    }
    cout << endl;
    return 0;
}