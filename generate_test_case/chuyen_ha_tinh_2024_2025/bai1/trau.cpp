// Thuật trâu: Tính từng kWh một, cộng dồn giá từng bậc (đúng tuyệt đối, không cần nhanh)

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int x1, x2, x3, x4;
    long long y;
    cin >> x1 >> x2 >> x3 >> x4 >> y;
    long long total = 0;
    for (long long i = 1; i <= y; ++i) {
        if (i <= 50)
            total += x1;
        else if (i <= 100)
            total += x2;
        else if (i <= 200)
            total += x3;
        else
            total += x4;
    }
    cout << total << endl;
    return 0;
}