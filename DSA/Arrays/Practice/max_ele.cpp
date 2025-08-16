#include <iostream>
#include <vector>
using namespace std;

// Function to find maximum in vector
int findMax(const vector<int>& v) {
    int maxElement = v[0];
    for(int i = 1; i < v.size(); i++) {
        if(v[i] > maxElement) {
            maxElement = v[i];
        }
    }
    return maxElement;
}

int main() {
    vector<int> nums = {5, 2, 8, 6, 3};

    int result = findMax(nums);
    cout << "Maximum element is: " << result << endl;

    return 0;
}
