#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> countMap;
        vector<int> result;

        // Count frequency of each number in nums1
        for (int num : nums1) {
            countMap[num]++;
        }

        // Check nums2 against map
        for (int num : nums2) {
            if (countMap[num] > 0) {
                result.push_back(num);
                countMap[num]--; // decrease count
            }
        }

        return result;
    }
};

int main() {
    vector<int> nums1 = {4, 9, 5};
    vector<int> nums2 = {9, 4, 9, 8, 4};

    Solution sol;
    vector<int> result = sol.intersect(nums1, nums2);

    cout << "[ ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << "]" << endl;

    return 0;
}
