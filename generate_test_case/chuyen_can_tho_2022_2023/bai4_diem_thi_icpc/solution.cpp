#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <algorithm>
using namespace std;

int main() {
    vector<tuple<int, char, string>> log;
    while (true) {
        int T;
        string P, R;
        cin >> T;
        if (T == -1) break;
        cin >> P >> R;
        log.push_back({T, P[0], R});
    }
    int total_time = 0, solved = 0;
    // Duyệt từng bài (A đến Z)
    for (char prob = 'A'; prob <= 'Z'; ++prob) {
        int penalty = 0, time = -1;
        bool solved_this = false;
        for (auto& entry : log) {
            int T;
            char P;
            string R;
            tie(T, P, R) = entry;
            if (P != prob) continue;
            if (!solved_this) {
                if (R == "wrong") penalty += 20;
                if (R == "right") {
                    time = T + penalty;
                    solved_this = true;
                }
            }
        }
        if (solved_this) {
            ++solved;
            total_time += time;
        }
    }
    cout << solved << " " << total_time << endl;
    return 0;
}