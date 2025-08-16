#include<iostream>
#include<vector>
using namespace std;
vector<int> PS(vector<int> nums, int target) {
    vector<int> result;
    int n = nums.size();
    
    // BRUTE FORCE APPROACH

    // for (int i = 0; i < n; i++) {
    //     for (int j = i + 1; j < n; j++) {
    //         if (nums[i] + nums[j] == target) {
    //             result.push_back(nums[i]);
    //             result.push_back(nums[j]);
    //             return result; // Return the first pair found
    //         }
    //     }
    // }

    // OPTIMIZED APPROACH 
    int i = 0;
    int j = n - 1;
    while(i < j) {
        int PS = nums[i] + nums[j];
        if(PS > target) {
            j--;
        } else if(PS < target) {
            i++;
        } else {
            result.push_back(nums[i]);
            result.push_back(nums[j]);
            return result;
        }
    }
    return result; // Return empty if no pair found
}

int main() {
    vector<int> arr = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = PS(arr, target);
    if (!result.empty())
        cout << result[0] << "," << result[1] << endl;
    else
        cout << "No pair found!" << endl;
    return 0;
}   