#include <iostream>
#include <vector>
using namespace std;

// Độ chính xác tuyệt đối, thuật trâu: Duyệt mọi j < i để tìm ngày xa nhất có a[j] < a[i]
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> a(n+1);
    for(int i=1;i<=n;++i) cin >> a[i];
    for(int i=1;i<=n;++i) {
        int res = 0;
        for(int j=1;j<i;++j) {
            if(a[j] < a[i]) res = i-j;
        }
        cout << res << (i==n ? '\n' : ' ');
    }
    return 0;
}