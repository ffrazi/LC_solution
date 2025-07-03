class Solution {
    public int shortestPathAllKeys(String[] grid) {
        int R= grid.length;
        int C= grid[0].length();
        boolean visited[][][] = new boolean[R][C][1<<6];
        Queue<int[]> queue = new LinkedList<>();
        int keys=0;
        for(int row=0; row<R; row++){
            for(int col=0;col<C;col++){
                char ch=grid[row].charAt(col);
                if(ch=='@'){
                    queue.add(new int[]{row,col,0,0});
                    visited[row][col][0] = true;
                }
                else if(ch>='a' && ch<='z'){
                    keys++;
                }
            }
        }
        int[][] diff = {{0,1},{1,0},{-1,0},{0,-1}};
        while(!queue.isEmpty()){
            int cell[] = queue.poll();
            int row = cell[0],col=cell[1],moves=cell[2],flag = cell[3];
            if (flag == ((1<<keys)-1)){
                return moves;
            }
            for(int i=0;i<4;i++){
                int ar=row+diff[i][0];
                int ac=col+diff[i][1];
                if(ar>=0 && ar< R && ac>=0 && ac<C){
                    char ch = grid[ar].charAt(ac);
                    if(ch=='#'){
                        continue;
                    }
                    if(ch>='A' && ch<='F'){
                        if ((flag & (1<<(ch-'A')))==0){
                            continue;
                        }
                    }
                    int new_flag = flag;
                    if(ch >='a' && ch<='f'){
                        new_flag = new_flag | (1<<(ch-'a'));
                    }
                    if(!visited[ar][ac][new_flag]){
                        queue.add(new int[]{ar,ac,moves+1,new_flag});
                        visited[ar][ac][new_flag]=true;
                    }
                }
            }
        }
        return -1;
    }
}