class Solution {
    int diff[][] = new int[][] { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

    private void dfs(int R, int C, char grid[][], int row, int col) {
        grid[row][col] = '0';
        for (int i = 0; i < 4; i++) {
            int adjR = row + diff[i][0];
            int adjC = col + diff[i][1];
            if (adjR >= 0 && adjR < R && adjC >= 0 && adjC < C) {
                if (grid[adjR][adjC] == '1') {
                    dfs(R, C, grid, adjR, adjC);
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        int R = grid.length, island = 0;
        int C = grid[0].length;
        boolean visited[][]=new boolean[R][C];
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < C; col++) {
                if (grid[row][col] == '1' && !visited[row][col]) {
                    island++;
                    dfs(R, C, grid, row, col);
                }
            }
        }
        return island;
    }
}