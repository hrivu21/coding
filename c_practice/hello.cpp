#include <bits/stdc++.h>
#define int long long int
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);
using namespace std;

const int N = 1000005;
int res[N];

void pp()
{
    vector<int> v;
    bool pr[N];
    memset(pr, true, sizeof(pr));

    for (int p = 2; p * p < N; ++p)
    {
        if (pr[p] == true)
        {
            for (int i = p * p; i < N; i += p)
                pr[i] = false;
        }
    }

    for (int p = 2; p < N; p++)
    {
        if (pr[p])
            v.push_back(p);
    }

    int count = 0;
    auto iiii = v.begin();

    int i = 0;
    for (i = 0; i < N; i++)
    {
        if (*iiii <= i)
        {
            iiii++;
            count++;
        }
        res[i] = count;
    }
}

signed main()
{
    fastio;
    pp();
    int T;
    cin >> T;
    while (T--)
    {
        int x, y;
        cin >> x >> y;
        if (res[x] > y)
            printf("Divyam\n");
        else
            printf("Chef\n");
    }
    return 0;
}
