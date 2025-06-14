#include <bits/stdc++.h>
using namespace std;

// Khai bao bien
int n;
int dinh_bat_dau;
vector<vector<int>> adj;
vector<bool> visited;

void docInput()
{
	cin >> n;
	
	adj.assign(n, vector<int>(n));
	visited.assign(n, false);
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> adj[i][j];
			
	cin >> dinh_bat_dau;
}

void dfs(int u)
{
	visited[u] = true;
	cout << u << " ";
	
	for (int v = 0; v < n; v++)
		if (adj[u][v] && !visited[v])
			dfs(v);
}

int main()
{
	docInput();
	dfs(dinh_bat_dau);
			
	return 0;
}