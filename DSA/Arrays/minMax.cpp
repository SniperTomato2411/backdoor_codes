#include<iostream>
using namespace std;

int getMax(int arr[], int n){
    int max = INT8_MIN;
    for(int i = 0; i < n; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

int getMin(int arr[], int n){
    int min = INT8_MAX;
    for(int i = 0; i < n; i++){
        if(arr[i] < min){
            min = arr[i];
        }
    }
    return min;
}

int main(){
    int size;
    int num[100];

    cout << "Enter the number of elements: ";
    cin >> size;

    cout << "Enter " << size << " elements: ";
    for(int i = 0; i < size; i++){
        cin >> num[i];
    }

    cout << "Maximum value in the array is: " << getMax(num, size) << endl;
    cout << "Minimum value in the array is: " << getMin(num, size) << endl;

    return 0;
}
