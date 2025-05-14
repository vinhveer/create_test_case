/*
Giải thích:
- Tính số tiền từng bậc, lần lượt trừ đi số điện đã tính ở các bậc trước.
- Cộng dồn: bậc 1: min(50, y); bậc 2: min(100-50, max(0, y-50)); bậc 3: min(200-100, max(0, y-100)); bậc 4: max(0, y-200)
- Độ phức tạp O(1), không tràn số.

*/

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream fi("PAY.INP");
    ofstream fo("PAY.OUT");
    int x1, x2, x3, x4;
    long long y;
    fi >> x1 >> x2 >> x3 >> x4 >> y;
    long long total = 0;
    total += min(50LL, y) * x1;
    if (y > 50) total += min(50LL, y-50) * x2;
    if (y > 100) total += min(100LL, y-100) * x3;
    if (y > 200) total += (y-200) * x4;
    fo << total << endl;
    return 0;
}