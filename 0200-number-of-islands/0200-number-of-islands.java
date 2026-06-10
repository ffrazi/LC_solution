class Solution {
    public int numIslands(char[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int cnt=0;

        int[][] dir={{-1,0},{1,0},{0,-1},{0,1}};

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                    cnt++;

                    Queue<int[]> q=new LinkedList<>();
                    q.offer(new int[]{i,j});
                    grid[i][j]='0';

                    while(!q.isEmpty()){
                        int[] cur=q.poll();
                        int x=cur[0];
                        int y=cur[1];

                        for(int[] d:dir){
                            int nx=x+d[0];
                            int ny=y+d[1];

                            if(nx>=0 && nx<m && ny>=0 && ny<n && grid[nx][ny]=='1'){
                                q.offer(new int[]{nx,ny});
                                grid[nx][ny]='0';
                            }
                        }
                    }
                }
            }
        }

        return cnt;
    }
}