#include <iostream>
#include <vector>
#include <string>
using namespace std;

string multiply(const string& num, int multiplier) {
    string result;
    int carry = 0;
    
    for (int i = num.size() - 1; i >= 0; i--) {
        int digit = (num[i] - '0') * multiplier + carry;
        carry = digit / 10;
        result = char(digit % 10 + '0') + result;
    }
    
    while (carry) {
        result = char(carry % 10 + '0') + result;
        carry /= 10;
    }
    
    return result;
}

string permutation(int n, int k) {
    if (k < 0 || n < 0) return "0";
    if (k > n) return "0";
    if (k == 0) return "1";
    
    string result = "1";

    for (int i = 0; i < k; i++) {
        result = multiply(result, n - i);
    }
    
    return result;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    cout << permutation(n, k) << endl;
    return 0;
}