class Cell{
    int row,col;
    public Cell(int r,int c){
        this.row=r;
        this.col=c;
    }
}
class Solution {
    public void solveSudoku(char[][] board) {
        int R=board.length;
        int C=board[0].length;
        int SIZE=board.length;
        int SMS=3;
        int rowf[]=new int[SIZE];
        int colf[]=new int[SIZE];
        int submatf[]=new int[SIZE];
        for(int row=0;row<R;row++){
            for(int col=0;col<C;col++){
                if(board[row][col]!='.'){
                    int dig= board[row][col]-'0';
                    rowf[row]|=(1<<dig);
                    colf[col]|=(1<<dig);
                    int submatidx=SMS*(row/SMS)+col/SMS;
                    submatf[submatidx]|=(1<<dig);
                }
            }
        }
        solve(R,C,SMS,board,rowf,colf,submatf);
    }
    private boolean solve(int R,int C,int SMS,char board[][],int rowf[],int colf[],int submatf[]){
        Cell toFill=getUnfilled(R,C,board);
        if(toFill==null){
            return true;
        }
        int submati=SMS*(toFill.row/SMS)+toFill.col/SMS;
        for(int dig=1;dig<=9;dig++){
            if((rowf[toFill.row]&(1<<dig))==0 && (colf[toFill.col]&(1<<dig))==0 && (submatf[submati]&(1<<dig))==0){
                board[toFill.row][toFill.col]=(char)('0'+dig);
                rowf[toFill.row]|=(1<<dig);
                colf[toFill.col]|=(1<<dig);
                submatf[submati]|=(1<<dig);
                boolean solved=solve(R,C,SMS,board,rowf,colf,submatf);
                if(solved){
                    return true;
                }
                board[toFill.row][toFill.col]='.';
                rowf[toFill.row]^=(1<<dig);
                colf[toFill.col]^=(1<<dig);
                submatf[submati]^=(1<<dig);
            }
        }
        return false;
    }
    private Cell getUnfilled (int R,int C,char board[][]){
        for (int row=0;row<R;row++){
            for(int col=0;col<C;col++){
                if (board[row][col]=='.'){
                    return new Cell(row,col);
                }
            }
        }
        return null;
    }

}