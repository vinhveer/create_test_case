#include <iostream>
#include <string>
using namespace std;

// Brute-force: thử tất cả các chữ số thay cho dấu ?, kiểm tra điều kiện tổng kiểm tra
int main() {
    string s;
    cin >> s;
    int n = s.size();
    int pos = -1; // vị trí dấu ?
    for (int i = 0; i < n; ++i)
        if (s[i] == '?') pos = i;
    // Vị trí đầu tiên luôn đọc được và khác 0 nên nếu pos==0 chỉ thử 1..9, còn lại 0..9
    int start_digit = (pos == 0 ? 1 : 0);
    int mul[7] = {9, 7, 3, 9, 7, 3, 9}; // Đủ cho 7 chữ số
    for (int d = start_digit; d <= 9; ++d) {
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            int val = (i == pos) ? d : (s[i] - '0');
            sum += val * mul[i];
        }
        if (sum % 10 == 0) {
            s[pos] = d + '0';
            cout << s << endl;
            return 0;
        }
    }
    // Nếu không tìm được, không ra đáp án (theo đề thì luôn có đáp án)
    return 0;
}