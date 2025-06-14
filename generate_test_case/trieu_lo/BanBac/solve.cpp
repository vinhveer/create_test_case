#include <iostream>
#include <vector>
using namespace std;

// Kiểm tra đồ thị vô hướng
bool isUndirected(const vector<vector<int>>& matrix) {
    int n = matrix.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (matrix[i][j] != matrix[j][i]) {
                return false;
            }
        }
    }
    return true;
}

// Tính bán bậc ra (out-degree) của mỗi đỉnh
vector<int> computeOutDegrees(const vector<vector<int>>& matrix) {
    int n = matrix.size();
    vector<int> outDegrees(n, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            outDegrees[i] += matrix[i][j];
        }
    }
    return outDegrees;
}

// Tính bán bậc vào (in-degree) của mỗi đỉnh
vector<int> computeInDegrees(const vector<vector<int>>& matrix) {
    int n = matrix.size();
    vector<int> inDegrees(n, 0);
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < n; ++i) {
            inDegrees[j] += matrix[i][j];
        }
    }
    return inDegrees;
}

// In danh sách giá trị, ngăn cách dấu ";"
void printDegrees(const vector<int>& degrees) {
    int n = degrees.size();
    for (int i = 0; i < n; ++i) {
        cout << degrees[i];
        if (i < n - 1) cout << ";";
    }
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    if (isUndirected(matrix)) {
        // Đồ thị vô hướng: in bậc của từng đỉnh
        vector<int> degrees = computeOutDegrees(matrix);
        printDegrees(degrees);
    } else {
        // Đồ thị có hướng: in bán bậc ra rồi bán bậc vào
        vector<int> outDegrees = computeOutDegrees(matrix);
        vector<int> inDegrees = computeInDegrees(matrix);
        printDegrees(outDegrees);
        cout << "\n";
        printDegrees(inDegrees);
    }

    return 0;
}