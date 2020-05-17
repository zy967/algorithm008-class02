class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int n = board.size(), m = n ? board[0].size():0;
        char& toClick = board[click[0]][click[1]];
        if (toClick == 'M') {
            toClick = 'X';
        }else {
            clickGrid(board, click[0], click[1]);
        }
        return board;
    }
    void clickGrid(vector<vector<char>>& board, int x, int y) {
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size() ||  board[x][y] != 'E') return;
        int nearMineNum = 0;
        vector<vector<int>> dirs = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}, {1,1}, {1, -1}, {-1,1}, {-1, -1}};
        for (int i = 0; i < dirs.size(); i++) {
            if (x+dirs[i][0] >= 0 && x+dirs[i][0] < board.size() && y+dirs[i][1] >= 0 && y+dirs[i][1] < board[0].size()) {
                if (board[x+dirs[i][0]][y+dirs[i][1]] == 'M') {
                    nearMineNum ++;
                }
            }
        }
        if (nearMineNum == 0) {
            board[x][y] = 'B';
            for (int i = 0; i < dirs.size(); i++) {
                if (x+dirs[i][0] >= 0 && x+dirs[i][0] < board.size() && y+dirs[i][1] >= 0 && y+dirs[i][1] < board[0].size()) {
                    clickGrid(board, x+dirs[i][0], y+dirs[i][1]);
                }
            }
        }else {
            board[x][y] = nearMineNum + '0';
        }
        return;
    }
};
