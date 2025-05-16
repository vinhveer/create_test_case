#include <bits/stdc++.h>
using namespace std;

// Returns true if 'c' is disallowed (i.e., appears in the string S).
bool isDisallowed(char c, const vector<bool>& disallowed) {
    return disallowed[c - '0'];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string P, S;
    cin >> P >> S;

    // Mark digits that should not appear in the result.
    // disallowed[d] = true means digit 'd' is forbidden.
    vector<bool> disallowed(10, false);
    for (char c : S) {
        disallowed[c - '0'] = true;
    }

    // We'll do a backtracking-like approach:
    // - Try to match digits of P from left to right.
    // - If the exact digit of P is not disallowed, place it and continue.
    // - If we get stuck, we reduce a previously matched digit and fill the rest with max allowed digits.
    // - If we cannot fix, answer is -1.

    // Convert P to a vector of digits for convenience.
    vector<int> digits(P.size());
    for (int i = 0; i < (int)P.size(); i++) {
        digits[i] = P[i] - '0';
    }

    // Attempt to construct the result in 'res'; start with -1 as sentinel.
    vector<int> res(P.size(), -1);

    // List of allowed digits in descending order (to fill from largest).
    vector<int> allowed;
    for (int d = 9; d >= 0; d--) {
        if (!disallowed[d]) {
            allowed.push_back(d);
        }
    }

    // If no digits are allowed at all, answer is -1.
    if (allowed.empty()) {
        cout << -1 << "\n";
        return 0;
    }

    // A helper function to fill the remaining positions with the largest possible allowed digits.
    auto fillMax = [&](int startPos){
        for (int i = startPos; i < (int)P.size(); i++) {
            res[i] = allowed[0];
        }
    };

    // We try to go digit by digit from left to right.
    // 'less' indicates whether we've already placed a digit smaller than P at an earlier position,
    // meaning we can freely fill the rest with largest allowed digits without worrying about P's constraint.
    bool less = false;
    for (int i = 0; i < (int)P.size(); i++) {
        int currentP = digits[i];
        bool placed = false;

        // If we are already strictly less, just place the largest allowed digit.
        if (less) {
            // place largest
            res[i] = allowed[0];
            continue;
        }

        // If we are not strictly less yet, we must be careful to not exceed currentP.
        // We'll try from currentP downward until we find an allowed digit.
        for (int d = currentP; d >= 0; d--) {
            if (!disallowed[d]) {
                res[i] = d;
                if (d < currentP) {
                    // We are now strictly less than P's digit here
                    less = true;
                }
                placed = true;
                break;
            }
        }

        if (!placed) {
            // We couldn't place any digit at position i with the condition <= currentP.
            // We need to backtrack to find a position that can be lowered.
            int j = i - 1;
            // Move left until we can reduce a digit.
            while (j >= 0) {
                int oldVal = res[j];
                // Attempt to find a smaller allowed digit than oldVal.
                // We search from oldVal-1 down to 0.
                bool found = false;
                for (int d = oldVal - 1; d >= 0; d--) {
                    if (!disallowed[d]) {
                        res[j] = d;
                        // Now fill the rest from j+1 to end with the largest allowed digits.
                        fillMax(j + 1);
                        found = true;
                        less = true; // definitely less
                        break;
                    }
                }
                if (found) {
                    break; // successfully backtracked
                } else {
                    // If we can't reduce res[j], set res[j] to -1 and keep going left
                    res[j] = -1;
                    j--;
                }
            }

            // If j < 0, we cannot backtrack.
            if (j < 0) {
                cout << -1 << "\n";
                return 0;
            }
            // If we backtracked successfully, done building.
            break;
        }
    }

    // If we've placed all digits or backtracked partially, we have a valid res.
    // Remove leading zeros if they appear. If result is empty, means 0 -> which might violate
    // the "positive integer" or if it has forbidden digits, also a problem. We'll check.
    // Typically, if the result is valid, it shouldn't have leading zeros unless the number is zero.
    int idx = 0;
    while (idx < (int)res.size() && res[idx] == 0) idx++;

    // If everything is zero, let's see if zero is allowed:
    bool allZero = true;
    for (int r : res) {
        if (r != 0) { allZero = false; break; }
    }
    // If allZero and 0 is allowed, we still have a valid "0" if it doesn't exceed P, but we need a positive integer.
    // The problem wants a positive integer, so a single '0' is not valid. We'll ignore that case, so -1 if all zero.
    if (allZero) {
        cout << -1 << "\n";
        return 0;
    }

    // Build string from res (skipping leading zeros).
    string ans;
    for (int i = idx; i < (int)res.size(); i++) {
        // If any digit is -1, that means the backtrack fix didn't fill properly -> -1.
        if (res[i] < 0) {
            cout << -1 << "\n";
            return 0;
        }
        ans.push_back((char)(res[i] + '0'));
    }
    if (ans.empty()) {
        // If the result is empty after trimming zeros -> -1
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }
    return 0;
}