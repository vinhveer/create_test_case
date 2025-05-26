#include <bits/stdc++.h>
using namespace std;

// Hàm đệ quy để tính đường đi có tổng lớn nhất
// i: hàng hiện tại, j: cột hiện tại
// n: số hàng, m: số cột
// grid: bảng chứa số lượng quà
int solveRecursive(vector<vector<int>>& grid, int i, int j, int n, int m) {
    // Nếu vượt quá giới hạn bảng
    if (i <= 0 || i > n || j <= 0 || j > m) {
        return -1e9; // Trả về giá trị âm lớn để không được chọn
    }

    // Đã đến cột cuối cùng
    if (j == m) {
        return grid[i][j];
    }

    // Có 3 lựa chọn di chuyển: (i-1,j+1), (i,j+1), (i+1,j+1)
    int moveUp = solveRecursive(grid, i-1, j+1, n, m);
    int moveRight = solveRecursive(grid, i, j+1, n, m);
    int moveDown = solveRecursive(grid, i+1, j+1, n, m);

    // Lấy giá trị lớn nhất từ 3 lựa chọn và cộng với giá trị ô hiện tại
    return grid[i][j] + max({moveUp, moveRight, moveDown});
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // Đánh chỉ số từ 1 để dễ xử lý
    vector<vector<int>> grid(n+1, vector<int>(m+1));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> grid[i][j];
        }
    }

    // Tìm đường đi tối ưu từ cột 1 đến cột m
    int maxGifts = -1;
    for (int startRow = 1; startRow <= n; startRow++) {
        int gifts = solveRecursive(grid, startRow, 1, n, m);
        maxGifts = max(maxGifts, gifts);
    }

    cout << maxGifts << "\n";
    return 0;
}