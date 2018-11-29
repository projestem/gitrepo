/*
 * horner.cpp
 * 
 * Copyright 2018  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <iostream>

using namespace std;

void drukujw(int st, float tbwsp[]){
    int i = 0;
    for(i = 0; i < st; i++){
        cout << tbwsp[i] << "x^" <<  st-i << " + ";
    }	
    cout << tbwsp[i] << endl;
}
  
    
}

int main(int argc, char **argv)
{
    
	int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp; // wskaźnik - zmienna przechowywująca adres komórki w pamięci
    tbwsp = new float [stopien+1];
    for (int  i = 0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
    }
    
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: " << horner_it(stopien, tbwsp, x);
    cout << endl;
    
	return 0;
}
