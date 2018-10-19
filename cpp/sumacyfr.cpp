/*
 * sumacyfr.cpp
 * 
 */


#include <iostream>

int sumuj_cyfry1(int liczba) {
    int suma = 0;
    while (liczba > 10 ) {
        suma += liczba % 10;
        liczba = liczba / 10;
    }
    return suma;
}

int main(int argc, char **argv)
{
	int liczba = 0; 
    while (liczba < 10) {
        cout << "Podaj liczbę 2-cyfrowa";
        cin >> liczba;
    }
        
    cout << "Suma: " << sumuj_cyfry1(liczba) <<
	return 0;
}

