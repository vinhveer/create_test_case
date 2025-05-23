#include <bits/stdc++.h>
using namespace std;

// Kiểm tra ký tự có phải dấu cách không
bool isNotSpace(char c) {
    return c != ' ';
}

// Kiểm tra xâu con từ vị trí [start, end] có chứa ký tự trùng lặp không
bool hasNoDuplicates(const string& s, int start, int end) {
    vector<bool> seen(256, false);  // Giả sử ASCII
    for (int i = start; i <= end; i++) {
        if (seen[s[i]]) {
            return false;  // Có ký tự trùng lặp
        }
        seen[s[i]] = true;
    }
    return true;
}

// Tìm xâu con không chứa ký tự trùng lặp, không có dấu cách, độ dài lớn nhất
string findPassword(const string& s) {
    int n = s.length();
    int maxLength = 0;
    string password = "";
    
    // Duyệt qua tất cả các xâu con có thể
    for (int start = 0; start < n; start++) {
        if (!isNotSpace(s[start])) continue;  // Bỏ qua nếu ký tự là dấu cách
        
        for (int end = start; end < n; end++) {
            if (!isNotSpace(s[end])) break;  // Dừng nếu gặp dấu cách
            
            // Kiểm tra xem xâu con từ start đến end có thỏa mãn không
            if (hasNoDuplicates(s, start, end)) {
                int length = end - start + 1;
                
                // Nếu độ dài lớn hơn hoặc bằng maxLength, cập nhật password
                if (length >= maxLength) {
                    maxLength = length;
                    password = s.substr(start, length);
                }
            }
        }
    }
    
    return password;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    cin.ignore();  // Bỏ qua ký tự xuống dòng sau khi đọc n
    
    while (n--) {
        string line;
        getline(cin, line);
        
        string password = findPassword(line);
        cout << password << endl;
    }
    
    return 0;
}