#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

// Function to check if a substring has all unique characters and no spaces
bool isValidPassword(const string& str) {
    unordered_set<char> seen;
    for (char c : str) {
        if (c == ' ') {
            return false; // Contains space
        }
        if (seen.find(c) != seen.end()) {
            return false; // Contains duplicate
        }
        seen.insert(c);
    }
    return true;
}

// Brute force function to find the longest valid password
string findPassword(const string& line) {
    string password = "";
    int maxLength = 0;
    
    // Check all possible substrings
    for (int i = 0; i < line.length(); i++) {
        for (int j = i; j < line.length(); j++) {
            string substr = line.substr(i, j - i + 1);
            
            // Check if valid and longer than current max
            if (isValidPassword(substr)) {
                if (substr.length() > maxLength) {
                    maxLength = substr.length();
                    password = substr;
                } else if (substr.length() == maxLength) {
                    // If same length, update to the later one
                    password = substr;
                }
            }
        }
    }
    
    return password;
}

int main() {
    int n;
    cin >> n;
    cin.ignore(); // Clear the newline
    
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        cout << findPassword(line) << endl;
    }
    
    return 0;
}