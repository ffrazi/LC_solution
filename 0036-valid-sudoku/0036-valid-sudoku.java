class Solution {
    public boolean isValidSudoku(char[][] board) {
        int size=board.length;
        int msize=3;
        int R=board.length;
        int C=board[0].length;
        int subarray[]=new int[size];
        int rows[]=new int[size];
        int cols[]=new int[size];
        for (int row=0;row<R;row++){
            for(int col=0;col<C;col++){
                if (board[row][col]!='.'){
                    int dig= board[row][col]-'0';
                    int subdig=msize*(row/msize)+(col/msize);
                    if((rows[row]&(1<<dig))!=0 || (cols[col]&(1<<dig))!=0 || (subarray[subdig]&(1<<dig))!=0){
                        return false;
                    }
                    rows[row]|=(1<<dig);
                    cols[col]|=(1<<dig);
                    subarray[subdig]|= (1<<dig);
                }
            }
        }
        return true;
    }
}