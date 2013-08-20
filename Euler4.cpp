/*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.*/
#include <iostream>
#include <string>
#include <sstream>
#include <ctime>

using namespace std;

string convert(int n);
string reverse_str(string s);
bool is_palindrome(int n);

int main(){
	clock_t t = clock();
	int highest_pal = 0;
	int limit = 999;

	for(int i = 100; i <= limit; i++){
		for(int j = 100; j <= limit; j++){
			int n = i * j;
			if(is_palindrome(n)){
				if(n > highest_pal){
					cout << "Highest Pal: " << n << "  with products: " << i << " and " << j << endl;
					highest_pal = n;
				}
			}
		}
	}
	t = clock() - t;
	cout << "Time it took: " << t/CLOCKS_PER_SEC << endl;
	cout << highest_pal;
	system("pause");
	return 0; 
}

string convert(int n){
   stringstream ss;//create a stringstream
   ss << n;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}


string reverse_str(string s){
	string result = "";
	for(int i = 0; i < s.length(); i++){
		result = s[i] + result;
	}
	return result;
}

bool is_palindrome(int n){
	string s = convert(n); //Convert n into a string s
	string rs = reverse_str(s); //Reverse the string s

	if(s == rs){
		return true;
	}
	else{
		return false;
	}
}