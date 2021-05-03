#include <bits/stdc++.h>
#include <vector>
using namespace std;

// void p(int x, int y)
// {
//     // long* j;
//     short c[2];
//     // j = &c[0];
//     // printf("%d\n", j);

//     printf("%d %d\n", &c[0], &c[1]);

//     printf("%d %d\n", x, y);
//     return;
// }

// int main()
// {
//     // printf("%c", getche());
//     // printf("Hello\n");

//     // char s0[20];
//     // char s1[20];
//     // scanf("%s%s", &s0, &s1);
//     // printf("%s%s\n", s0, s1);

//     // printf("%s\n", "********");
//     // gets(s1);
//     // printf("%s", s1);
//     // puts(s1);

//     // int a = 1;
//     // int b = 2;
//     // p(a, b);
//     // printf("%d %d %d", a, ++a, a++);

//     int x = 10;
//     // printf("%d", x++);
//     // printf("%d", 36>>2);
//     int a = 0, z = 10;
//     z = (a++) ? 1 : 0;
//     printf("%d", z);
// }

int main()
{
	int n;
	cin >> n;

    vector<int> vect;
    vect.assign(n, 0);

    int q;
    for(int i=0; i<n; i++){
    	cin >> vect[i];
    }

    cout << vect[0] << ' ' << vect[1] << endl;
}
