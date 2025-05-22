#include <bits/stdc++.h>
using namespace std;

// Đảo ngược từng từ, giữ nguyên số lượng và vị trí khoảng trắng
// Sau đó tìm từ dài nhất (sau đảo), in ra cùng vị trí xuất hiện

int main() {
    string S;
    getline(cin, S);

    int n = S.size();
    string result;
    vector<pair<string, int>> words; // (word, start_pos)
    int i = 0;
    while (i < n) {
        if (S[i] == ' ') {
            // Ghi các khoảng trắng liên tiếp
            result += S[i];
            ++i;
        } else {
            // Bắt đầu một từ
            int start = i;
            string word;
            while (i < n && S[i] != ' ') {
                word += S[i];
                ++i;
            }
            // Đảo ngược từ
            reverse(word.begin(), word.end());
            result += word;
            words.emplace_back(word, result.size() - word.size() + 1); // vị trí xuất hiện (tính từ 1)
        }
    }
    cout << result << "\n";

    // Tìm từ dài nhất
    int maxLen = 0;
    for (auto &w : words) maxLen = max(maxLen, (int)w.first.size());

    // In ra các từ dài nhất, theo thứ tự xuất hiện, mỗi dòng: từ vị trí
    for (auto &w : words) {
        if ((int)w.first.size() == maxLen) {
            cout << w.first << " " << w.second << "\n";
        }
    }
    return 0;
}