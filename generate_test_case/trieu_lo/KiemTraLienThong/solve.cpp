#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;
vector<bool> visited;

void input()
{
	cin >> n;
	
	adj.assign(n, vector<int>(n));
	visited.assign(n, false);
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> adj[i][j];
}

void dfs(int u)
{
	visited[u] = true;
	
	for (int i = 0; i < n; i++)
		if (adj[u][i] == 1 && !visited[i])
			dfs(i);
}

int main()
{
	input();
	dfs(0);
	
	for (int value : visited)
	{
		if (value == false)
		{
			cout << "khong lien thong";
			return 0;
		}
	}
	
	cout << "lien thong";
	
	return 0;
}