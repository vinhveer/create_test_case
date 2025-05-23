#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    int m;
    cin >> S >> m;

    int n = S.size();
    // Tạo mảng lưu số lần cần đảo ngược tại mỗi vị trí
    vector<int> reverse_count(n + 1, 0);

    // Đọc m thao tác và đánh dấu hiệu ứng đảo ngược
    for (int i = 0; i < m; i++) {
        int k;
        cin >> k;
        // Bắt đầu đảo từ vị trí k-1 (0-based)
        reverse_count[k - 1]++;
        // Kết thúc hiệu ứng đảo tại vị trí n-k
        reverse_count[n - k]--;
    }

    // Tích lũy số lần đảo ngược đang được áp dụng
    int curr_reverses = 0;
    // Duyệt đến giữa chuỗi; mỗi lần xét vị trí i và đối xứng n-i-1
    for (int i = 0; i < n / 2; i++) {
        curr_reverses += reverse_count[i];
        // Nếu số lần đảo lẻ, thì swap ký tự hai đầu
        if (curr_reverses % 2 != 0) {
            swap(S[i], S[n - i - 1]);
        }
    }

    cout << S << '\n';
    return 0;
}
