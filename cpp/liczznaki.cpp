/*
 * liczznaki.cpp
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>
 */
 
 
#include <iostream>
 
using namespace std;
 
void licz_znaki(char tb[], int roz){
    //for(int i = 0; i < roz; i++){
        //cout << tb[i];
    //}
    int i = 0;
    int biale, literyD, literyM, reszta;
    biale = literyD = literyM = reszta = 0;
    int znak_kod = 0;
    while(tb[i] != '\0'){
        znak_kod = (int)tb[i];
        if(znak_kod > 64 && znak_kod < 91)
            literyD++;
        else if(znak_kod > 96 && znak_kod < 123)
            literyM++;
        i++;
        }
    cout << "Białych: " << biale << endl;
    cout << "Duże: " << literyD << endl;
    cout << "Małe: " << literyM << endl;
    cout << "Reszta: " << reszta << endl;
}
 
int main(int argc, char **argv)
{
    const int rozmiar = 21;
    char znaki[rozmiar]; // max 20 znaków ostatni to \0
    cin.getline(znaki, 21);
    licz_znaki(znaki, rozmiar);
        return 0;
}
