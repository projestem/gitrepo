/*
 * zad3.cpp
 * 
 * 
 */


#include <iostream>

using namespace std;                          

int main()
{    
    int liczba;
    int suma = 0;
    int podzielnych = 0;
    
    // wczytaj 8 liczb
    for(int i=0;i<8;++i)
    {
        cin >> liczba;
        suma += liczba;
        if(liczba % 5 == 0) podzielnych++;
    }
    
    cout << "Suma: " << suma << endl;
    cout << "Srednia: " << suma/8.0 << endl;
    cout << "Podzielnych przez 5: " << podzielnych << endl;
    
    cin.get();
    cin.ignore(1);
    
    return 0;
}

