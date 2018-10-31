/*
 * znaki.cpp
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
void licz_znaki(char tab[])
{   
    int i = 0;
    int biale = 0;
    
    while(tab[i] != '\0')
    {
        if (tab[i] == ' ' || tab[i] == '\t')
            biale++;
        else
        cout << tab[i];  
        i++;
                
    }
    
    cout << "\nZnaków białych: " << biale << endl;
}
int main(int argc, char **argv)
{
	const int rozmiar = 20;  // deklaracja stałej
    
    char znaki[rozmiar];  // deklaracja tablicy znakowej (character - znak)
    
    cout << "Jak się nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Cześć " << znaki << endl;
    
    licz_znaki(znaki);
    
	return 0;
}
