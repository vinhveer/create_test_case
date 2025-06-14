#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Prototypes
void InputArray(vector<string>& arr);
vector<string> SubtractionProcess(vector<string> setA, vector<string> setB);
void PrintArrayAsc(vector<string> arr);
bool IsNumeric(const string& s);
bool Compare(const string& a, const string& b);

int main() {
    vector<string> setA;
    vector<string> setB;
    
    InputArray(setA);
    InputArray(setB);
    
    PrintArrayAsc(SubtractionProcess(setA, setB));
    
    return 0;
}

void InputArray(vector<string>& arr) {
    int size;
    cin >> size;
    
    string temp;
    
    for (int i = 0; i < size; i++) {
        cin >> temp;
        arr.push_back(temp);
    }
}

vector<string> SubtractionProcess(vector<string> setA, vector<string> setB) {
    vector<string> results;
    
    for (string valueA : setA) {
        bool exist = false;
        
        // Check if valueA exists in set B
        for (string valueB : setB) {
            if (valueA == valueB) {
                exist = true;
                break;
            }
        }
        
        // If not in set B, check if already in results
        if (!exist) {
            bool already_in_result = false;
            for (string elem : results) {
                if (elem == valueA) {
                    already_in_result = true;
                    break;
                }
            }
            
            // Only add to results if not already there
            if (!already_in_result) {
                results.push_back(valueA);
            }
        }
    }
    
    return results;
}

void PrintArrayAsc(vector<string> arr) {
    if (arr.empty()) {
        cout << "none";
        return;
    }
    
    sort(arr.begin(), arr.end(), Compare);
    
    for (string value : arr)
        cout << value << " ";
}

bool IsNumeric(const string &s) {
    if (s.empty()) return false;
    for (char c : s)
        if (!isdigit(c))
            return false;
    return true;
}

bool Compare(const string& a, const string& b) {
    bool a_is_number = IsNumeric(a);
    bool b_is_number = IsNumeric(b);
    
    if (a_is_number != b_is_number) {
        return a_is_number;
    }
    
    return a < b;
}