#include<iostream>
#include<vector>
using namespace std;

int sum(int arr[], int n){
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    return sum;
}
int main(){
    int arr[] = {10,-5,20};
    int n = sizeof(arr)/sizeof(arr[0]); // Calculate the number of elements in the array
    int result = sum(arr, n);
    cout << "Sum of elements in the array: " << result << endl;
    return 0;
}