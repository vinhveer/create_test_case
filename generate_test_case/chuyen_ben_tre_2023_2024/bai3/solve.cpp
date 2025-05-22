#include <bits/stdc++.h>

using namespace std;

int main()
{

    cin.tie(0);
    ios_base::sync_with_stdio(false);
    cout.tie(0);

    string s;

    getline(cin, s);

    long long i = 0;

    while (i < s.size() - 1)
    {

        if (s[i] - '0' <= s[i + 1] - '0')
        {

            s.erase(s.begin() + i);
        }
        else
        {

            i++;
        }
    }

    cout << s << endl;

    return 0;
}