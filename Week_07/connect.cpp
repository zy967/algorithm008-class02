class Solution {
public:
    
    void connect(vector<vector<char>>& board, int row, int col)
    {   
        if(row < 0 || row >= board.size() || col < 0 || col >= board[row].size())
        {
            return;
        }
        
        if(board[row][col] == 'O')
        {
            board[row][col] = 'Y';
            connect(board, row + 1, col);
            connect(board, row - 1, col);
            connect(board, row, col + 1);
            connect(board, row, col - 1);
        }
        else
        {
            return;
        }
        
    }
    
    void solve(vector<vector<char>>& board) {
        if(board.empty())
        {
            return;
        }
        // up line
        int row = 0;
        for(int i = 0; i < board[row].size(); i++)
        {
            if(board[row][i] == 'O')
            {
                board[row][i] = 'Y';
                connect(board, row + 1, i);
                connect(board, row, i + 1);
            }
        }
        
        // bottom line
        row = board.size() - 1;
        for(int i = 0; i < board[row].size(); i++)
        {
            if(board[row][i] == 'O')
            {
                board[row][i] = 'Y';
                connect(board, row - 1, i);
                connect(board, row, i + 1);
            }
        }
        
        int col = 0;
        for(int i = 0; i < board.size(); i++)
        {
            if(board[i][col] == 'O')
            {
                board[i][col] = 'Y';
                connect(board, i, col + 1);
                connect(board, i + 1, col);
            }
        }
        
        col = board[0].size() - 1;
        for(int i = 0; i < board.size(); i++)
        {
            if(board[i][col] == 'O')
            {
                board[i][col] = 'Y';
                connect(board, i, col - 1);
                connect(board, i + 1, col);
            }
        }
        
        for(row = 0; row < board.size(); row++)
        {
            for(col = 0; col < board[row].size(); col++)
            {
                if(board[row][col] == 'O')
                {
                    board[row][col] = 'X';
                } 
                else if(board[row][col] == 'Y')
                {
                    board[row][col] = 'O';
                }
            }
        }
    }
};
