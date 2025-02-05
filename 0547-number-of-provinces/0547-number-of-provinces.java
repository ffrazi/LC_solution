class Solution {
    private void dfs(int N,int city,int isConnected[][],boolean visited[]){
        visited[city]=true;
        for (int othCity=0;othCity<N;othCity++){
            if(!visited[othCity] && isConnected[city][othCity]==1){
                dfs(N,othCity,isConnected,visited);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int N=isConnected.length,province=0;
        boolean visited[]=new boolean[N];
        for(int city=0;city<N;city++){
            if(!visited[city]){
                province++;
                dfs(N,city,isConnected,visited);
            }
        }
        return province;
    }
}