#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    string n;
    cin >> n;
    int res = 0;
    for (char c : n) {
        if (c == '-') continue; // Bỏ qua dấu âm
        int digit = c - '0';
        res = max(res, digit);
    }
    cout << res << endl;
    return 0;
}