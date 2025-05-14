#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    getline(cin, S);
    for (char &c : S) {
        if ('a' <= c && c <= 'z') c = c - 'a' + 'A';
    }
    cout << S << endl;
    return 0;
}