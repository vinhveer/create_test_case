#include <bits/stdc++.h>
using namespace std;

// A helper function to convert a number to its string representation
string numToStr(long long x) {
    ostringstream oss;
    oss << x;
    return oss.str();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    cin >> k;  // 1 <= k <= 1e14
    
    // Step 1: Find the block of d-digit numbers where the k-th digit is located.
    // Each d-digit block has "9 * 10^(d-1)" numbers, each contributes d digits.
    // So the block size in digits is blockSize = 9 * 10^(d-1) * d.
    // We'll subtract these block sizes from k until we find which block contains the k-th digit.
    
    long long d = 1;        // current digit length we are considering
    long long base = 9;     // 9 * 10^(d-1) for d=1
    long long blockSize = 9;  // blockSize for d=1 is 9 * 1 = 9
    
    while(true) {
        blockSize = base * d;  // 9*10^(d-1)*d
        if(k <= blockSize) {
            break;
        }
        k -= blockSize;
        d++;
        base *= 10;   // for next d, base = 9*10^(d-1)
    }

    // Step 2: Now we know k is in the block of d-digit numbers.
    // The starting number for d-digit block is "startNum = 10^(d-1)".
    // offset (0-based) in the block is (k-1). 
    // So the actual number index offsetNumberInBlock = (k-1)/d  (integer division).
    // the digit inside that number is digitIndex = (k-1)%d.
    
    long long startNum = 1;
    for(int i = 1; i < d; i++) {
        startNum *= 10;  // 10^(d-1)
    }
    
    long long offsetNumberInBlock = (k - 1) / d;  // which number (0-based) in d-digit block
    long long digitIndex = (k - 1) % d; // which digit (0-based) in that number
    
    // The actual number that holds the k-th digit
    long long actualNumber = startNum + offsetNumberInBlock;
    
    // Step 3: We'll build the sequence of digits from that point onward
    // We need 4 consecutive digits a_k, a_{k+1}, a_{k+2}, a_{k+3}.
    // Start by building a string from actualNumber, actualNumber+1, etc., 
    // until we accumulate at least (digitIndex + 4) digits in the buffer.
    
    // We'll do a simple approach: keep appending digits from consecutive numbers 
    // until we have enough digits to extract our 4 consecutive digits starting at digitIndex.
    
    // Note: We might cross the boundary from d-digit to (d+1)-digit numbers if close enough, 
    // so keep generating next numbers if needed until we have enough digits.
    
    // We'll just generate up to 30 or so consecutive numbers, which is definitely enough to cover 4 digits
    // even if we cross to a new digit length. This "brute force" approach ensures correctness.
    
    string buffer;
    long long currNumber = actualNumber;
    while((long long)buffer.size() < digitIndex + 4) {
        buffer += numToStr(currNumber);
        currNumber++;
    }
    
    // Step 4: Extract the 4 digits from the buffer
    string result = buffer.substr(digitIndex, 4);
    
    cout << result << "\n";
    return 0;
}