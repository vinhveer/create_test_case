#include <bits/stdc++.h>
using namespace std;

// Độ chính xác tuyệt đối, xử lý N lớn <= 5e17, đọc N dạng string

int main() {
    string N;
    int K;
    cin >> N >> K;

    vector<int> digits;
    for (char c : N)
        digits.push_back(c - '0');
    sort(digits.rbegin(), digits.rend()); // Sắp xếp giảm dần

    // Lấy chữ số lớn thứ K
    cout << digits[K-1] << '\n';
    return 0;
}