#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;  // initially set to max possible
        int maxProfitVal = 0;    // initially no profit

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;  // update min if lower price found
            }
            if (price - minPrice > maxProfitVal) {
                maxProfitVal = price - minPrice;  // update max profit
            }
        }
        return maxProfitVal;
    }
};

int main() {
    vector<int> prices = {7, 1, 5, 3, 6, 4}; // sample stock prices

    Solution sol;
    int profit = sol.maxProfit(prices);

    cout << "Maximum Profit: " << profit << endl;

    return 0;
}
