#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int n;
int x1, x2;
int max_x1;
int min_x2 = INT_MAX;


int main() {
    cin >> n;

    for (int i =0; i < n; i++){
        cin >> x1 >> x2;
        max_x1 = max(max_x1, x1);
        min_x2 = min(min_x2, x2);
    }

    if (max_x1 <= min_x2)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}