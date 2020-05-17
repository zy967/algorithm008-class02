class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0, n = grid.size(), m = n ? grid[0].size() : 0; // In case the vector is empty
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (isIsland(grid, i, j)) {
                    count += 1;
                }
            }
        }
        return count;
    }

    bool isIsland(vector<vector<char>>& grid, int i, int j) {
        if (i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size()) {
            char c = grid[i][j];
            if (grid[i][j] == '1'){
                grid[i][j] = '0';
                isIsland(grid, i+1, j);
                isIsland(grid, i, j+1);
                isIsland(grid, i-1, j);
                isIsland(grid, i, j-1);
                return true;
            }
        }
        return false;
    }
};
