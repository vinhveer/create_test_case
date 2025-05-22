#include <iostream>
#include <vector>

using namespace std;

// Function to count divisors of a number
int countDivisors(int n) {
    int count = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            // If divisors are equal, count only one
            if (n / i == i)
                count++;
            else // Otherwise count both
                count += 2;
        }
    }
    return count;
}

// Function to count special numbers in range [L, R]
int countSpecialNumbers(int L, int R) {
    int count = 0;
    for (int i = L; i <= R; i++) {
        if (countDivisors(i) == 4)
            count++;
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int L, R;
        cin >> L >> R;
        cout << countSpecialNumbers(L, R) << endl;
    }
    
    return 0;
}