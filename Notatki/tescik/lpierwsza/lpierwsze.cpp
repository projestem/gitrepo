#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Podaj liczbe: ";
    cin >> n;
    int i = 2;
    while(i*i<=n){
        if(n % i == 0){
            cout << "Liczba zlozona";
            return 0;
        } else i++;
    }
    cout << "Liczba pierwsza";
    return 0;
}
