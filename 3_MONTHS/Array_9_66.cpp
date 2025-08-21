// #include<iostream>
// #include<vector>
// using namespace std;

// vector<int> plusOne(vector<int>& digits){
//     for(int i=digits.size()-1;i>=0;i++){
//         if(digits[i] == 9){
//             digits[i]=0;
//         }
//         else{
//             digits[i] += 1;
//             return digits;
//         }
//     }
//     digits.insert(digits.begin(), 1);
//     return digits;
// }

// int main(){
//     vector<int> l1={1,2,7,1,9,9,9};

//     vector<int> result = plusOne(l1);

//     cout<<"[ ";
//     for(int num : result){
//         cout<<num<<" ";
//     }
//     cout<<"]";

//     return 0;
// }


#include<iostream>
#include<vector>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
    int carry = 1; // because we want to add 1

    for (int i = digits.size() - 1; i >= 0; i--) {
        int sum = digits[i] + carry;
        digits[i] = sum % 10;
        carry = sum / 10;
    }

    if (carry) { // still a carry after loop
        digits.insert(digits.begin(), carry);
    }

    return digits;
}

int main() {
    vector<int> l1 = {1,2,3,4,5,6,7,8,9,9,9,9,9,9};
    vector<int> result = plusOne(l1);

    cout << "[ ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << "]\n";

    return 0;
}
