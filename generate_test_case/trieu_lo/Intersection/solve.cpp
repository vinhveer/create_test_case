#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// Prototype
void InputArray(vector<int>& arr);
vector<int> IntersectionProcess(vector<int>& setA, vector<int>& setB);
void PrintArrayAsc(vector<int> arr);

int main()
{
	vector<int> setA;
	vector<int> setB;
	
	InputArray(setA);
	InputArray(setB);
	
	PrintArrayAsc(IntersectionProcess(setA, setB));
	
	return 0;
}

void InputArray(vector<int>& arr)
{
	int size;
	cin >> size;
	
	int temp;
	
	for (int i = 0; i < size; i++)
	{
		cin >> temp;
		arr.push_back(temp);
	}
}

vector<int> IntersectionProcess(vector<int>& setA, vector<int>& setB)
{
	vector<int> results;
	
	for (int valueB : setB)
	{
		bool exist = false;
		for (int valueA : setA)
			if (valueA == valueB)
			{
				exist = true;
				break;
			}
		
		if (exist) results.push_back(valueB);
	}
	
	return results;
}

void PrintArrayAsc(vector<int> arr)
{
	if (arr.empty())
	{
		cout << "none";
		return;
	}
	
	sort(arr.begin(), arr.end());
	
	bool first = true;
	for (int value : arr) {
	    if (!first) 
	        cout << " ";
	    cout << value;
	    first = false;
	}
}