#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int m, n, k;
    cin >> m >> n >> k;
    
    vector<pair<int, int>> cherries(4 * k);
    for (int i = 0; i < 4 * k; i++) {
        cin >> cherries[i].first >> cherries[i].second;
    }
    
    // Count valid ways to cut the cake
    long long count = 0;
    
    // Try all possible horizontal cuts (between rows)
    for (int h_cut = 1; h_cut < m; h_cut++) {
        // Try all possible vertical cuts (between columns)
        for (int v_cut = 1; v_cut < n; v_cut++) {
            // Count cherries in each quadrant
            int top_left = 0, top_right = 0, bottom_left = 0, bottom_right = 0;
            
            for (const auto& cherry : cherries) {
                int row = cherry.first;
                int col = cherry.second;
                
                if (row <= h_cut && col <= v_cut) {
                    top_left++;
                } else if (row <= h_cut && col > v_cut) {
                    top_right++;
                } else if (row > h_cut && col <= v_cut) {
                    bottom_left++;
                } else { // row > h_cut && col > v_cut
                    bottom_right++;
                }
            }
            
            // Check if all quadrants have exactly k cherries
            if (top_left == k && top_right == k && bottom_left == k && bottom_right == k) {
                count++;
            }
        }
    }
    
    cout << count << endl;
    return 0;
}