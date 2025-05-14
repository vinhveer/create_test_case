#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

struct ProblemInfo {
    int wrong_count = 0;
    int accepted_time = -1;
    bool solved = false;
};

int main() {
    unordered_map<char, ProblemInfo> problems;
    while (true) {
        int T;
        string P, R;
        cin >> T;
        if (T == -1) break;
        cin >> P >> R;
        char prob = P[0];
        auto& info = problems[prob];
        if (info.solved) continue;
        if (R == "wrong") info.wrong_count++;
        else if (R == "right") {
            info.accepted_time = T + info.wrong_count * 20;
            info.solved = true;
        }
    }
    int solved = 0, total = 0;
    for (auto& kv : problems) {
        if (kv.second.solved) {
            solved++;
            total += kv.second.accepted_time;
        }
    }
    cout << solved << " " << total << endl;
    return 0;
}