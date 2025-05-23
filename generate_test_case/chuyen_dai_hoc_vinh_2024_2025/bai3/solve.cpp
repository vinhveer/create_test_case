#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define pb push_back
#define pf push_front
#define pll pair<ll,ll>
#define fs(i,l,r) for(ll i=(l);i<=(r);i++)
#define fb(i,r,l) for(ll i=(r);i>=(l);i--)
const ll N = 1E6+5;
const ll mod = 1E9+7;
using namespace std;

bool check(char c) {
    return c != ' ';
}

string get(string s) {
    unordered_map<char, ll> mp;
    ll start = 0, max_length = 0, max_start = 0;
    ll n = s.size();
    
    for(ll end = 0; end < n; ++end) {
        if(!check(s[end])) {
            start = end + 1;
            mp.clear();
            continue;
        }
        
        if(mp.find(s[end]) != mp.end() && mp[s[end]] >= start) {
            start = mp[s[end]] + 1;
        }
        
        mp[s[end]] = end;
        
        if(end - start + 1 >= max_length) {
            max_length = end - start + 1;
            max_start = start;
        }
    }
    
    return s.substr(max_start, max_length);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    
    // freopen(".INP","r",stdin);
    // freopen(".OUT","w",stdout);
    
    ll q; 
    cin >> q;
    cin.ignore();
    
    while(q--) {
        string s;
        getline(cin, s);
        string ans = get(s);
        cout << ans << '\n';
    }
    
    return 0;
}
