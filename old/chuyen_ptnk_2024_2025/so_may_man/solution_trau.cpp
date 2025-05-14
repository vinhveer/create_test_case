#include <iostream>
#include <vector>
using namespace std;

int find_lucky_card(int n) {
    vector<int> cards;
    for (int i = 1; i <= n; ++i) {
        cards.push_back(i);
    }

    while (cards.size() > 1) {
        vector<int> new_cards;
        for (size_t i = 0; i < cards.size(); ++i) {
            if (i % 3 == 1) {
                new_cards.push_back(cards[i]);
            }
        }
        cards = new_cards;
    }

    return cards[0];
}

int main() {
    int n;
    cin >> n;
    cout << find_lucky_card(n) << endl;
    return 0;
}
