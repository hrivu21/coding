#include<bits/stdc++.h>
#include<iostream>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<math.h>

using namespace std;


template <typename T>   // use of generic
string str_vector(vector<T> v){
    string s = "[ ";
    for(auto i: v){
        s += to_string(i) + " ";
    }
    return s+"]";
}




using namespace std;

class Point{
    public:
        int x, y;
    public:
        Point(int a, int b){
            x = a;
            y = b;
        }
};
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

// struct point{
//     int x, y;
// };

string pp(Point p){
    return to_string(p.x) + " " + to_string(p.y);
}


int f(vector<bool>& arr){
    int c = 0;
    for(auto n: arr){
        c += n;
        n = n^1;
    }
    return c;
}



void f1(){
        vector<bool> v = {1,1,0};
    cout << v[0] << v[1] << v[2] << endl;
    cout << f(v) << endl;
    cout << v[0] << v[1] << v[2] << endl;
    cout <<  v.size() <<  endl;

    cout << floor(5/3) << endl;
}


void f2(){
    int n = (int)pow(2,10) ;
    n >>= 3;
    bool w = ((n >> 9) & 1) && ((n >> 8) & 1) && ((n >> 7) & 1);
    cout << w << n << endl;
}


void pass_vector2D_by_reference(vector<vector<int>> &matrix){   // pass by reference

    for(int i=0; i<matrix.size(); i++){
        for(int j=0; j<matrix[0].size(); j++){
            cout << matrix[i][j] << " ";

            matrix[i][j] *= (-1);
        }
        cout << endl;
    }
}


void bitset_operation(){
    int n = 8;
    bitset<sizeof(int)> bits(n);
    cout << bits[3] << endl;
}



int main()
{
	// vector<Point*> arr;
 //    Point p1(2, 2);
 //    // struct point p = {1,1};
 //    arr.push_back(&p1);
 //    cout << pp(*arr[0]) << endl;
 //    p1.x = 1;
 //    cout << pp(*arr[0]) << endl;

    // Point p1(1,1);
    // Point& p2 = p1;

    // auto x = &p1 == &p2;
    // cout << x << endl;

    // Point& p2 = p1;

    // p2.x = 5;

    // cout << pp(p1) << endl;
    // cout << pp(p2) << endl;

    // bool a = 10;
    // cout << (a+1) << endl;




    // f2();




    // vector<vector<int>> mat(3, vector<int>(2, -1));
    // for(int i=0; i<3; i++){
    //     for(int j=0; j<2; j++){
    //         cin >> mat[i][j];
    //     }
    // }
    // pass_vector2D_by_reference(mat);
    // cout << mat[0][0]<< endl;

    bitset_operation();
    return 0;

}
