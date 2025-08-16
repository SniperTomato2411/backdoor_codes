#include<iostream>
#include<vector> 
using namespace std;
int main(){
    int n=5;
    int arr[5]={1,2,3,4,5};

    int ms=INT8_MIN;
    int cs=0;
    for(int st=0;st<n;st++){
        int CS=0;
        for(int end=st;end<n;end++){
            // for(int i=st;i<=end;i++){
            //     cout<<arr[i];    
            // }
            // cout<<" ";

            CS+=arr[end];
            ms=max(ms,CS);
        }
        // cout<<endl; 
    }

    cout<<"Maximum Subarray Sum: "<<ms<<endl;
    return 0;
}