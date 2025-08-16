#include <iostream>
using namespace std;
void update(int arr[], int n)
{   
    cout<<"Inside the main function" << endl;

    arr[0] = 120; // Updating the first element of the array
    // Printing the array before update
    for(int i=0;i<3;i++){
        cout<<arr[i]<<" ";
    }
    cout << endl;
    cout << "Going back to main" << endl;
}
int main()
{
    int arr[3] = {1, 2, 3};
    update(arr, 3);

    // Printing the array after update
    for (int i = 0; i < 3; i++)
    {
        cout << arr[i] << " ";
    }
}