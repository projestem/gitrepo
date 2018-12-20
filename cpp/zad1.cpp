/*
 * zad1.cpp
 * 
 */


#include <iostream>

using namespace std;
 
int main() 
{
    int sum = 0;
    for (int i = 10; i < 100 ; i+= 2)
    {
        sum += i;
    }
    cout << sum;
}
