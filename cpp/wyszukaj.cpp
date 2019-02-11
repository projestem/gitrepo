/*
 * sortowanie.cxx
 */
 
 
 
#include <iostream>
 
using namespace std;
 
void wypelnij(int t[], int roz){
    srand(time(NULL)); // Inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < roz; i++){
        t[i] = rand() % 101;
    }
}
 
void drukuj(int t[], int roz){
    for(int i = 0; i < roz; i++){
        cout << t[i] << " ";
    }
    cout << endl;
}
 
void sort_insert(int tab[], int n){
    int i, el, k;
    for(i = 1; i < n; i++){
        el = tab[i];
        k = i - 1;
        while(k >= 0 && tab[k] > el){
            tab[k+1]=tab[k];
            k--;
        }
        tab[k+1]=el;
    }
}
 
int szukaj_lin(int tab[], int n, int szuk){
    
    for(int i=0; i < n; i++){
        if(tab[i] == szuk)
            return 1;
    }
    return -1;
}
 
int main(int argc, char **argv)
{
        int n = 20;
    int tab[n];
    wypelnij(tab, n);
    drukuj(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: "; cin >> szuk;
    int indeks = szukaj_lin(tab, n, szuk);
    if (indeks != -1)
        cout << "Znaleziono!";
    else
        cout << "Nie znaleziono!";
    return 0;
}
 
