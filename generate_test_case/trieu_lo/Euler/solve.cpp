#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

// Hàm kiểm tra đồ thị liên thông (sử dụng BFS)
bool isConnected(int n, const vector<vector<int>>& adjacencyMatrix) {
    vector<bool> visited(n, false);
    queue<int> q;

    // Tìm đỉnh đầu tiên có bậc > 0
    int start = -1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (adjacencyMatrix[i][j] > 0) {
                start = i;
                break;
            }
        }
        if (start != -1) break;
    }

    // Nếu không có cạnh nào trong đồ thị, coi như liên thông
    if (start == -1) return true;

    // Bắt đầu BFS
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int i = 0; i < n; ++i) {
            if (adjacencyMatrix[node][i] > 0 && !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }

    // Kiểm tra tất cả các đỉnh có bậc > 0 đã được thăm hay chưa
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (adjacencyMatrix[i][j] > 0 && !visited[i]) {
                return false;
            }
        }
    }

    return true;
}

// Hàm kiểm tra đồ thị liên thông mạnh (cho đồ thị có hướng)
bool isStronglyConnected(int n, const vector<vector<int>>& adjacencyMatrix) {
    // BFS kiểm tra liên thông từ tất cả các đỉnh
    for (int start = 0; start < n; ++start) {
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            for (int i = 0; i < n; ++i) {
                if (adjacencyMatrix[node][i] > 0 && !visited[i]) {
                    visited[i] = true;
                    q.push(i);
                }
            }
        }

        // Kiểm tra nếu có đỉnh nào chưa được thăm
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) return false;
        }
    }

    return true;
}

// Hàm kiểm tra đồ thị Euler
string checkEulerianGraph(int n, const vector<vector<int>>& adjacencyMatrix, bool isDirected) {
    if (!isDirected) {
        // Kiểm tra đồ thị vô hướng
        if (!isConnected(n, adjacencyMatrix)) {
            return "khong_phai_do_thi_Euler";
        }

        // Đếm số đỉnh bậc lẻ
        int oddDegreeCount = 0;
        for (int i = 0; i < n; ++i) {
            int degree = 0;
            for (int j = 0; j < n; ++j) {
                degree += adjacencyMatrix[i][j];
            }
            if (degree % 2 != 0) {
                oddDegreeCount++;
            }
        }

        if (oddDegreeCount == 0) {
            return "do_thi_Euler"; // Chu trình Euler
        } else if (oddDegreeCount == 2) {
            return "do_thi_nua_Euler"; // Đường đi Euler
        } else {
            return "khong_phai_do_thi_Euler";
        }
    } else {
        // Kiểm tra đồ thị có hướng
        if (!isStronglyConnected(n, adjacencyMatrix)) {
            return "khong_phai_do_thi_Euler";
        }

        vector<int> inDegree(n, 0), outDegree(n, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                outDegree[i] += adjacencyMatrix[i][j];
                inDegree[j] += adjacencyMatrix[i][j];
            }
        }

        int inMinusOut1 = 0, outMinusIn1 = 0;
        for (int i = 0; i < n; ++i) {
            if (outDegree[i] - inDegree[i] == 1) {
                outMinusIn1++;
            } else if (inDegree[i] - outDegree[i] == 1) {
                inMinusOut1++;
            } else if (inDegree[i] != outDegree[i]) {
                return "khong_phai_do_thi_Euler";
            }
        }

        if (inMinusOut1 == 0 && outMinusIn1 == 0) {
            return "do_thi_Euler"; // Chu trình Euler
        } else if (inMinusOut1 == 1 && outMinusIn1 == 1) {
            return "do_thi_nua_Euler"; // Đường đi Euler
        } else {
            return "khong_phai_do_thi_Euler";
        }
    }
}

int main() {
    int n;
    bool isDirected;
    cin >> n;
    cin >> isDirected;

    vector<vector<int>> adjacencyMatrix(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> adjacencyMatrix[i][j];
        }
    }

    // Kiểm tra và in kết quả
    string result = checkEulerianGraph(n, adjacencyMatrix, isDirected);
    cout << result << endl;

    return 0;
}