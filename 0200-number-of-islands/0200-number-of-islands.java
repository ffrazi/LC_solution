class Solution {
    void change(char a[][],int i,int j){
        if(i<0 || j<0 ||i==a.length||j==a[0].length||a[i][j]!='1'){
            return;
        }
        a[i][j]=5;
        change(a,i-1,j);
        change(a,i+1,j);
        change(a,i,j-1);
        change(a,i,j+1);
    }
    public int numIslands(char[][] grid) {
        int c=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1'){
                    c++;
                    change(grid,i,j);
                }
            }
        }
        return c;
    }
}