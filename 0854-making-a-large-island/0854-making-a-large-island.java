import java.util.*;

class Solution {
    int[][] diff = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; 

    public int largestIsland(int[][] grid) {
        int R = grid.length;
        int C = grid[0].length, isl = 0;
        boolean[][] visited = new boolean[R][C];

        // Mark islands with unique ids
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, i, j, R, C, visited, ++isl);
                }
            }
        }

        int[] count = new int[isl + 1];
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < C; col++) {
                if (grid[row][col] != 0) {
                    count[grid[row][col]]++;
                }
            }
        }

        int max = 0;
        for (int i = 1; i <= isl; i++) {
            max = Math.max(max, count[i]);
        }

        // Now check each 0 to flip and calculate possible max island
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < C; col++) {
                if (grid[row][col] == 0) {
                    Set<Integer> adj = new HashSet<>();
                    for (int i = 0; i < 4; i++) {
                        int ar = row + diff[i][0];
                        int ac = col + diff[i][1];
                        if (ar >= 0 && ar < R && ac >= 0 && ac < C && grid[ar][ac] != 0) {
                            adj.add(grid[ar][ac]);
                        }
                    }
                    int cur = 1;
                    for (int i : adj) {
                        cur += count[i];
                    }
                    max = Math.max(max, cur);
                }
            }
        }

        return max;
    }

    private void dfs(int[][] grid, int row, int col, int R, int C, boolean[][] visited, int isl) {
        visited[row][col] = true;
        grid[row][col] = isl; // mark the island id in the grid

        for (int i = 0; i < 4; i++) {
            int adjR = row + diff[i][0];
            int adjC = col + diff[i][1];

            if (adjR >= 0 && adjR < R && adjC >= 0 && adjC < C && !visited[adjR][adjC]) {
                if (grid[adjR][adjC] == 1) {
                    dfs(grid, adjR, adjC, R, C, visited, isl);
                }
            }
        }
    }
}