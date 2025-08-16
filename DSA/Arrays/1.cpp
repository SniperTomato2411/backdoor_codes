#include<iostream>
using namespace std;
void printArray(int arr[],int n){

    cout<<"Printing the array: ";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";

    }
    cout<<"Printing DONE!" << endl;
}

int main(){
    int num[15];

    cout<<"Value at 15 index " << num[0] << endl; 
    cout<<"Value at  20 index " << num[20] << endl; 

    int second[3]={5,2,3};
    cout<<"Value at 2 index " << second[2] << endl;

    int third[14]={2,5};
    // cout<<"Value at 13 index " << third[13] << endl;
    int n=5;
    // cout<<"Printing the array: ";
    // for(int i=0;i<n;i++){
    //     cout<<third[i]<<" ";
    // }
    printArray(third, 14);

    int thirdsize= sizeof(third)/sizeof(int);
    cout<<"Size of third array: " << thirdsize << endl; 

    int fourth[10]={0};
    // // cout<<"Value at 0 index " << fourth[0] << endl;
    int a=5;
    // // cout<<"Printing the array: ";
    // // for(int i=0;i<a;i++){
    // //     cout<<fourth[i]<<" ";
    // // }
    printArray(fourth, 10);

    int fifth[10]={1};
    // cout<<"Value at 0 index " << fifth[0] << endl;
    int b=10;
    // cout<<"Printing the array: ";
    // for(int i=0;i<b;i++){
    // cout<<fifth<<" ";
    // }

    printArray(fifth, 10);

    int fifthsize= sizeof(fifth)/sizeof(int );
    cout<<"Size of fifth array: " << fifthsize << endl;
     
    int sixth[15] = {2,7};
    int j=8;
    printArray(sixth, 8);
    
    char ch[5]= {'a', 'b', 'c', 'd', 'e'};
    cout<<ch[3] << endl;
    
    
    
    cout<< endl << endl<< "Everything is fine!" << endl << endl;

    

    return 0;
}

