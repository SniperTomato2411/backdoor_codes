#include <iostream>
#include <vector>
using namespace std;

int singleNumber(vector<int> &nums)
{
    int ans = 0;
    for (int val : nums)
    {
        ans ^= val;
    }
    return ans;
}

int main()
{
    vector<int> nums = {2, 2, 1,1,3,3,4,4,6};

    int singleNumber1 = singleNumber(nums);

    // if(singleNumber1){
    //     cout<<"Ok";
    // }
    // else{
    //     cout<<"Not Okay";
    // }

    cout << "The single number is " << singleNumber1 << endl;

    return 0;
}