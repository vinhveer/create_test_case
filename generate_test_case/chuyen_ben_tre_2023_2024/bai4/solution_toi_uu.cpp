#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Trả về max(min(a[i]*a[j], b[i]*b[j])) với i ≠ j
int main() {
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;

    // Tìm 2 phần tử lớn nhất trong a và b cùng chỉ số
    int maxa1=-1, maxa2=-1, ia1=-1, ia2=-1;
    for(int i=0;i<n;++i) {
        if (a[i]>maxa1) {maxa2=maxa1; ia2=ia1; maxa1=a[i]; ia1=i;}
        else if (a[i]>maxa2) {maxa2=a[i]; ia2=i;}
    }
    int maxb1=-1, maxb2=-1, ib1=-1, ib2=-1;
    for(int i=0;i<n;++i) {
        if (b[i]>maxb1) {maxb2=maxb1; ib2=ib1; maxb1=b[i]; ib1=i;}
        else if (b[i]>maxb2) {maxb2=b[i]; ib2=i;}
    }

    int ans = 0;

    // Xét các cặp (i,j) với max trong a, hoặc max trong b
    vector<pair<int,int>> candidates;
    candidates.push_back({ia1, ib1});
    candidates.push_back({ia1, ib2});
    candidates.push_back({ia2, ib1});
    candidates.push_back({ia2, ib2});
    for(int i=0;i<n;++i) {
        if (i!=ia1) candidates.push_back({ia1,i});
        if (i!=ib1) candidates.push_back({i,ib1});
    }

    for(auto p : candidates) {
        int i = p.first, j = p.second;
        if (i==j) continue;
        int A = a[i]*a[j];
        int B = b[i]*b[j];
        ans = max(ans, min(A,B));
    }
    cout << ans << endl;
    return 0;
}