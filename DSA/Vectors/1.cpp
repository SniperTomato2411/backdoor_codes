// #include<iostream>
// #include<vector>
// using namespace std;

// int main(){
//     vector<int> vec;
//     cout<<vec[0]<<endl;

//     vector<int> vec1 = {1,2,3};
//     cout<<vec1[0];
//     return 0;

// }

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // vector<int> vec;
    // cout << vec[0] << endl; // ⚠️ undefined behavior

    // vector<int> vec1 = {1, 2, 3};
    // cout << vec1[0]<<endl;

    // vector<int> vec1(5,0);
    // cout << vec1[0]<<endl;

    // vector<char> vec={'a','b','c','d','e'};

    vector<int> vec;
    vec.push_back(23);
    vec.push_back(29);
    vec.push_back(24);

    cout << "Size = " << vec.size() << endl;
    vec.push_back(23);
    // vec.push_back(24);
    // cout<<"Size= "<<vec.size()<<endl;
    cout<<"After pushback the size= "<<vec.size()<<endl;


    for(char val : vec){
        cout<<val<<endl;
    }

    return 0;
}
