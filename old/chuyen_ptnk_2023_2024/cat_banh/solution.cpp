#include <bits/stdc++.h>
using namespace std;

/*
  Brute force approach for the "Cắt bánh" problem:

  - We'll maintain a 2D grid (M x N) marking positions of cherries.
  - Construct a 2D prefix sum array P where:
       P[x][y] = number of cherries in the sub-rectangle (1..x, 1..y).
  - The total number of cherries is 4 * K.
  - For each possible horizontal cut h in [1..M-1], and each possible vertical cut v in [1..N-1]:
       - We can compute the number of cherries in each of the 4 quadrants:
         top-left = sum in (1..h, 1..v)
         top-right = sum in (1..h, v+1..N)
         bottom-left = sum in (h+1..M, 1..v)
         bottom-right = sum in (h+1..M, v+1..N)
       - Check if each quadrant has exactly K cherries.
       - If yes, increment our answer counter.
  - Output the final count.

  This solution is O(M*N) in checking, plus the cost of building prefix sums,
  which is absolutely huge for M,N up to 1e5 (10^10 operations). 
  However, it is correct for smaller inputs (and is indeed a brute force solution).
*/

static long long getPrefixSum(const vector<vector<long long>>& P, int x, int y) {
    // get prefix sum P up to (x, y)
    // clamp x,y to range
    if(x < 0 || y < 0) return 0;
    return P[x][y];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N, K;
    cin >> M >> N >> K; // 1 <= M, N <= 1e5, 1 <= K <= 5e4
    // total cherries = 4*K

    // We'll build a 2D array for cherries, 1-based indexing for convenience.
    // But to handle large M,N, we do note that this can be huge in memory (M*N can be up to 1e10).
    // As stated, this is a brute force approach, not feasible for large M,N in practice.
    // We'll still demonstrate the code for correctness.

    // Warning: in practice, you cannot even allocate such an array if M*N ~ 1e10.
    // This code is purely illustrative for the brute force idea on smaller constraints.

    // For demonstration here, we do 0-based indexing with a vector of size (M+1)*(N+1).
    // This is still impossible for large M,N, but consistent with the brute force requirement.

    vector<vector<long long>> grid(M+1, vector<long long>(N+1, 0LL));
    for(int i = 0; i < 4*K; i++){
        int x, y;
        cin >> x >> y;
        // put a cherry at (x, y)
        grid[x][y] = 1;
    }

    // Build prefix sums
    vector<vector<long long>> P(M+1, vector<long long>(N+1, 0LL));
    for(int x = 1; x <= M; x++){
        long long rowSum = 0;
        for(int y = 1; y <= N; y++){
            rowSum += grid[x][y];
            P[x][y] = P[x-1][y] + rowSum;
        }
    }

    // We'll define a lambda to get the sum of cherries in the sub-rectangle (r1..r2, c1..c2).
    auto rectSum = [&](int r1, int c1, int r2, int c2){
        if(r1 > r2 || c1 > c2) return 0LL;
        return P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1];
    };

    // The 4 quadrants for a cut at (h, v):
    // top-left:     (1..h,   1..v)
    // top-right:    (1..h,   v+1..N)
    // bottom-left:  (h+1..M, 1..v)
    // bottom-right: (h+1..M, v+1..N)

    long long ans = 0;
    for(int h = 1; h < M; h++){
        for(int v = 1; v < N; v++){
            long long tl = rectSum(1, 1, h, v);
            if(tl != K) continue; // quick skip if top-left != K

            long long tr = rectSum(1, v+1, h, N);
            if(tr != K) continue;

            long long bl = rectSum(h+1, 1, M, v);
            if(bl != K) continue;

            long long br = rectSum(h+1, v+1, M, N);
            if(br != K) continue;

            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}