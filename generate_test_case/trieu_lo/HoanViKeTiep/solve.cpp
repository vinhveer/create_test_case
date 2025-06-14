#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to print a permutation
void printPermutation(const vector<int> &perm)
{
    for (int num : perm)
    {
        cout << num;
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;

    // Initialize the first permutation: 1, 2, ..., n
    vector<int> perm(n);
    for (int i = 0; i < n; ++i)
    {
        perm[i] = i + 1;
    }

    // Print the first permutation
    printPermutation(perm);

    // Generate and print all subsequent permutations
    while (next_permutation(perm.begin(), perm.end()))
    {
        printPermutation(perm);
    }

    return 0;
}