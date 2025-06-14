#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void InputArray(vector<int>& arr);
void UnionProcess(vector<int>& setA, const vector<int>& setB);
void PrintArrayWithAsc(const vector<int>& arr);

int main()
{
    vector<int> setA;
    vector<int> setB;
    
    InputArray(setA);
    InputArray(setB);
    
    // N?i hai vector l?i v?i nhau (concat)
    setA.insert(setA.end(), setB.begin(), setB.end());
    
    // S?p x?p tang d?n và lo?i b? ph?n t? trùng
    sort(setA.begin(), setA.end());
    setA.erase(unique(setA.begin(), setA.end()), setA.end());
    
    PrintArrayWithAsc(setA);
    
    return 0;
}

void InputArray(vector<int>& arr)
{
    int size;
    cin >> size;
    
    arr.resize(size);
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
}

void PrintArrayWithAsc(const vector<int>& arr)
{
    for (int value : arr)
        cout << value << " ";
}