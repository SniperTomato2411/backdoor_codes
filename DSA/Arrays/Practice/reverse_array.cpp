#include<iostream>
#include<vector>
using namespace std;

int revArray(int arr[], int n){
    int start=0;
    int end=n-1;

    while(start<end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}

int main(){
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(arr[0]); // Calculate the number of elements in the array
    revArray(arr, n);
    cout << "Reversed array: ";
    for(int i=0;i<n;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}