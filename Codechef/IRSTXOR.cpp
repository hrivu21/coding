#include <iostream>
#include <string>
using std::string;
using namespace std;

string toBin(int n)
{
    if (n == 0)
        return "0";
    string b = "";
    while (n > 0)
    {
        b = to_string(n % 2) + b;
        n /= 2;
    }
    return b;
}

int f(int c)
{
    string C = toBin(c);
    string a = "1";
    string b = "0";
    for (int i = 1; i < C.length(); i++)
    {
        if (C[i] == '1')
        {
            b += "1";
            a += "0";
        }
        else
        {
            b += "1";
            a += "1";
        }
    }
    return (stoi(a, 0, 2) * stoi(b, 0, 2));
}

int main()
{
    int t;
    cin >> t;
    int c[t];
    for (int i = 0; i < t; i++)
    {
        cin >> c[i];
        cout << f(c[i]) << endl;
    }
    return 0;
}