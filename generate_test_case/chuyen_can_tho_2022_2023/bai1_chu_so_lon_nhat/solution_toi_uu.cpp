#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ifstream fin("CSLN.INP");
    ofstream fout("CSLN.OUT");
    string n;
    fin >> n;
    int max_digit = 0;
    for (char c : n) {
        if (c == '-') continue;
        int digit = c - '0';
        if (digit > max_digit) max_digit = digit;
        if (max_digit == 9) break; // Tối ưu: dừng khi gặp 9
    }
    fout << max_digit << endl;
    return 0;
}