#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    cin >> S;
    string res = "";
    for(char c : S) {
        // Nếu res rỗng hoặc c < kí tự cuối cùng thì thêm vào
        if (res.empty() || c < res.back())
            res += c;
        else {
            // Nếu c >= res.back(), tìm vị trí phù hợp để nối vào sau các kí tự nhỏ hơn
            int k = res.size();
            while (k > 0 && res[k-1] <= c) k--;
            if (k == 0) res = c;
            else res = res.substr(0, k) + c;
        }
    }
    cout << res << '\n';
    return 0;
}