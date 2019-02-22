#include <iostream>
using namespace std;
#define MAKS 100

char przesun_litere(char litera, int klucz){
    int kod=(int) litera;

    if (kod>=65 && kod <=90) {
        // Duża litera
        kod+=klucz;
        if (kod>90) {
            kod-=26;
        }else if(kod<65){
            kod+=26;
        }
    }else if(kod>=97 && kod <=122){
        // Mała litera
        kod+=klucz;
        if (kod>122) {
            kod-=26;
        }else if(kod<97){
            kod+=26;
        }
    }
    
    return (char) kod;
}


void wyswietl(char tekst[], int n){
    for(int i=0;i<n;i++){
        cout<<tekst[i];
    }
}


void szyfruj(char tekst[], int klucz, int n){
    klucz%= 26;
    
    for(int i=0;i<n;i++)
        tekst[i]=przesun_litere(tekst[i], klucz);
    
    wyswietl(tekst, n);
}
    

int main()
{
    // pobierz dane wejsciowe
    
    char tekst[MAKS];
    int klucz;
    cin.getline(tekst, MAKS);
    cin >> klucz;
    
    int n=cin.gcount()-1;

    //lower(tekst, n);
    szyfruj(tekst, klucz, n);
    cout<<endl;
    szyfruj(tekst, -klucz, n);
    
	
	return 0;
}
