#include<iostream>
#include<vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0; // handle empty case

    int k = 1; // first element is always unique
    for (int j = 1; j < nums.size(); j++) {
        if (nums[j] != nums[j - 1]) {
            nums[k] = nums[j];
            k++;
        }
    }
    return k;
}

int main() {
    vector<int> l1 = {1, 1, 2};

    int k = removeDuplicates(l1);

    cout << "k = " << k << endl;
    cout << "[ ";
    for (int i = 0; i < k; i++) {
        cout << l1[i] << " ";
    }
    cout << "]" << endl;

    return 0;
}
