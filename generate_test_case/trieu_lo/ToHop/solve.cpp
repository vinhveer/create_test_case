#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Helper function to multiply a string number by an integer
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

// Helper function to divide a string number by an integer
string divide(const string& num, int divisor) {
    string result;
    int remainder = 0;
    
    for (char digit : num) {
        int current = remainder * 10 + (digit - '0');
        result += char(current / divisor + '0');
        remainder = current % divisor;
    }
    
    // Remove leading zeros
    size_t startpos = result.find_first_not_of("0");
    if (startpos != string::npos) {
        result = result.substr(startpos);
    } else {
        result = "0";
    }
    
    return result;
}

// Calculate combination using string-based arithmetic
string combination(int n, int k) {
    if (k < 0 || n < 0) return "0";
    if (k > n) return "0";
    if (k == 0 || k == n) return "1";
    
    // Use symmetry property
    if (k > n - k) k = n - k;
    
    string result = "1";
    for (int i = 1; i <= k; i++) {
        result = multiply(result, n - i + 1);
        result = divide(result, i);
    }
    
    return result;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    cout << combination(n, k) << endl;
    return 0;
}