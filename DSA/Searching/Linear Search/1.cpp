#include<iostream>
using namespace std;

bool linearSearch(int arr[], int n, int key){
    for(int i=0;i<n;i++){
        if(arr[i] == key){
            return true; // Element found
        }
    }
    return 0;

}
int main(){

    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // Whether 1 is present in the array or not
    cout<<"Enter the key to search: ";
    int key;
    cin>>key;
    // Call the linearSearch function
    bool found = linearSearch(arr, 10, key);
    if(found){
        cout<<"Element found in the array!"<<endl;
    } else {
        cout<<"Element not found in the array!"<<endl;
    }
    return 0;

}