#include<iostream>
#include<vector>
using namespace std;

void rev(vector<int>& nums, int start, int end){
    while(start<=end){
        int temp= nums[start];
        nums[start]=nums[end];
        nums[end]= temp;
        start++,end--;
    }
}
void rotate(vector<int>&nums,int k){
    int n=nums.size();
    if(n==0 || k%n==0) return;
    k%=n;

    rev(nums,0,n-1);
    rev(nums,0,k-1);
    rev(nums,k,n-1);
}
int main(){
    vector<int> l1={1,2,3,4,5};
    // rev(l1,0,l1.size()-1);
    int k=3;
    rotate(l1,k);
    for(int nums : l1){
        cout<<nums<<" ";
    }
    cout<<endl;
    return 0;
    
}