#include<iostream>
using namespace std;
    int addSum(int a,int b){
        return a+b;

    }
int main(){
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    int sum = addSum(a, b);
    cout << "The sum is: " << sum << endl;
    return 0; 
}