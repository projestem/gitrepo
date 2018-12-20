/*
 * zad2.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

int main()
{
    double a,b,c;
    cin>>b>>c;
    do
    {
        a=b;
        b=c;
        cin>>c;
    }
    while(c!=a*b);
    cout<<c;
    return 0;
}
