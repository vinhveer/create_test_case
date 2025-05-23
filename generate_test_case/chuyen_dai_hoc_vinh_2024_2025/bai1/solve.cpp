#include <iostream>
using namespace std;

bool isPrime(int n) {
    // Check if a number is prime
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int sumOfDigits(int n) {
    // Calculate the sum of digits of a number
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int countEmirpNumbers(int L, int R) {
    // Check constraints
    if (!(1 < L && L <= R && R <= 1000000)) {
        return -1;
    }
    
    int count = 0;
    for (int num = L; num <= R; num++) {
        if (isPrime(num) && isPrime(sumOfDigits(num))) {
            count++;
        }
    }
    return count;
}

int main() {
    int L, R;
    cin >> L >> R;
    
    int result = countEmirpNumbers(L, R);
    cout << result << endl;
    
    return 0;
}
