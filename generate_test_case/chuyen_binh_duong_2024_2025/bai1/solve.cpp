/*
Giải thích cách giải tối ưu:
- Ta biết chỉ có đúng 1 dấu hỏi ở vị trí i, và các thừa số cho từng vị trí đã biết trước.
- Gọi S là tổng kiểm tra của các chữ số đã biết (giả sử coi ?=0).
- Gọi x là chữ số thay cho '?', thừa số là mul[i].
- Ta cần tìm x sao cho (S + x * mul[i]) % 10 == 0, với ràng buộc nếu i==0 thì x từ 1..9, còn lại 0..9.
- Tìm x trực tiếp không cần thử tất cả.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    int mul[7] = {9, 7, 3, 9, 7, 3, 9};
    int pos = -1, S = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '?') pos = i;
        else S += (s[i] - '0') * mul[i];
    }
    int x = -1;
    // Tìm x thỏa mãn (S + x*mul[pos])%10==0
    int start_digit = (pos == 0 ? 1 : 0);
    for (int d = start_digit; d <= 9; ++d) {
        if ((S + d * mul[pos]) % 10 == 0) {
            x = d;
            break;
        }
    }
    s[pos] = x + '0';
    cout << s << endl;
    return 0;
}