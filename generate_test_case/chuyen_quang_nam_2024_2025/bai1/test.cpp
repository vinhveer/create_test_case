#include <bits/stdc++.h>
using namespace std;

vector<long long> fibo_list(long long n)
{

    vector<long long> list;

    long long a = 1, b = 1;

    list.push_back(a);

    while (b <= n)
    {

        list.push_back(b);

        long long temp = a + b;

        a = b;

        b = temp;
    }

    return list;
}

int main()
{

    cin.tie(0);
    ios_base::sync_with_stdio(false);
    cout.tie(0);

    long long n;

    cin >> n;

    vector<long long> fibo = fibo_list(n);

    vector<long long> res;

    long long sum = 0;

    for (long long i = fibo.size() - 1; i >= 0; i--)
    {

        if (fibo[i] <= n)
        {

            res.push_back(fibo[i]);

            n -= fibo[i];
        }
        

        if (n == 0)
            break;
    }

    for (long long num : res)
    {

        cout << num << " ";
    }

    return 0;
}