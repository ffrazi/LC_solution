class Solution {
    public void solve(char[][] board) {
        int r=board.length;
        int c = board[0].length;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(board[i][j] == 'O' && (i == 0 || i == r - 1 || j == 0 || j == c - 1))
                {
                        change(board,i,j);
                }
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(board[i][j] == 'O')
                    board[i][j] = 'X';
                if(board[i][j]=='R')
                    board[i][j] = 'O';
            }
        }
    }
    void change(char[][] board,int r,int c)
    {
        if(r<0 || c<0 || r>=board.length || c>=board[0].length || board[r][c]!='O')
            return;
        board[r][c] = 'R';
        change(board,r-1,c);
        change(board,r+1,c);
        change(board,r,c-1);
        change(board,r,c+1);
    }
}