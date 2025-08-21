#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool containsDuplicate(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i] == nums[i + 1])
        {
            return true;
        }
    }

    return false;
}

int main()
{
    vector<int> nums = {1, 2, 3, 1};                // Create the input vector

    bool hasDuplicate = containsDuplicate(nums);    // Call the function

    if (hasDuplicate)                               // Show result
    {
        cout << "Found" << endl;
    }
    else
    {
        cout << "Not found" << endl;
    }
}