#include<iostream>
using namespace std;

int binarySearch(int arr[], int key, int size) {
    int start = 0;
    int end = size - 1;

    while(start <= end){
        int mid = start + (end - start) / 2;  // better for avoiding overflow

        if(arr[mid] == key){
            return mid;
        }

        if(key > arr[mid]){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
    }

    return -1;  // if not found
}

int main() {
    int even[6] = {2, 4, 6, 8, 10, 12};
    int odd[5] = {1, 3, 5, 7, 9};

    int index = binarySearch(even, 1, 6); // key = 12, size = 6
    int index1 = binarySearch(odd, 1, 5);  // key = 1, size = 5

    cout << "Index of 1 is " << index << endl;
    cout << "Index of 1 is " << index1 << endl;

    return 0;
}
