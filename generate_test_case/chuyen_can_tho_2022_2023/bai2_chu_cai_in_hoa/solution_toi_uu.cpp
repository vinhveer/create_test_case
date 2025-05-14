#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    getline(cin, S);
    for (char &c : S) {
        if (c >= 'a' && c <= 'z') c &= ~32;
    }
    cout << S << '\n';
    return 0;
}