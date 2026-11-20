#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        memo.assign(m, vector<int>(n, -1));
        return dfs(0, 0, m, n);
    }

private:
    vector< vector<int> > memo;

    int dfs(int i, int j, int m, int n)
    {
        if (i == m - 1 && j == n - 1) // Reached goal
            return 1;

        if (i >= m || j >= n) // Out of bounds
            return 0;

        if (memo[i][j] != -1) // have we already solved this cell
            return memo[i][j];

        memo[i][j] = dfs(i, j + 1, m, n) + dfs(i + 1, j, m, n);

        return memo[i][j];
    }
};