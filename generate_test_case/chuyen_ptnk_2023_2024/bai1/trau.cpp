#include <bits/stdc++.h>
using namespace std;

/*
  Thuật trâu (Brute Force) cho bài tìm lá bài may mắn.

  Ý tưởng:
  - Xuất phát với một danh sách các lá bài {1, 2, 3, ..., n}.
  - Trong mỗi bước:
    + Lần lượt trải các lá bài từ vị trí 1 đến vị trí hiện có (1-based).
    + Giữ lại các lá bài ở vị trí i sao cho i % 3 == 2 (tức i ≡ 2 mod 3).
    + Bỏ các lá bài còn lại.
  - Tiếp tục lặp cho đến khi còn đúng 1 lá bài duy nhất. Đó là lá bài may mắn.

  Nhược điểm:
  - Chi phí thời gian và bộ nhớ cực lớn khi n lên đến 10^9.
  - Chỉ đảm bảo độ chính xác nếu giả lập được đầy đủ trên máy tính có đủ tài nguyên.
  - Không tối ưu về bộ nhớ cũng như tốc độ, nhưng đáp ứng yêu cầu "thuật trâu" về tính đúng đắn.
*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    // Với n rất lớn (lên đến 10^9), giải pháp này hầu như không khả thi trong thực tế do giới hạn bộ nhớ.
    // Tuy nhiên, về mặt lý thuyết, đây là cách mô phỏng trực tiếp "thuật trâu".

    vector<long long> cards(n);
    // cards: [1, 2, ..., n]
    for(long long i = 0; i < n; i++){
        cards[i] = i + 1;
    }

    // Lặp cho đến khi còn 1 lá bài
    while(cards.size() > 1){
        vector<long long> newCards;
        // Giữ lại các lá bài ở vị trí i mà i % 3 == 2 (i tính từ 1)
        for(long long i = 1; i <= (long long)cards.size(); i++){
            if(i % 3 == 2){
                newCards.push_back(cards[i - 1]);
            }
        }
        cards = move(newCards);
    }

    // Xuất kết quả
    cout << cards[0] << "\n";

    return 0;
}