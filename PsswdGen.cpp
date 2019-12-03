// PasswdGenerator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Developed by 0X1347 Inc.
#include "pch.h"
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main() {
	cout << "\t\t\t\t\t 0X1347 Inc."<< endl;
	cout << "Enter The Length Of The Password :  ";
	int x;
	cin >> x;
	srand(time(0));
	cout << "The Password :";
	for (int y = 1; y < x+1; y++) {
		int DecNum;
		DecNum = (rand() % 93 + 33);
		cout << (char) DecNum ;
		}
	   
	cout << endl;
	}
