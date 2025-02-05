import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        int R = grid.length, C = grid[0].length;
        boolean[][] visited = new boolean[R][C];
        Queue<int[]> queue = new LinkedList<>();
        int days = -1, oranges = 0;

        for (int row = 0; row < R; row++) {
            for (int col = 0; col < C; col++) {
                if (grid[row][col] != 0) {
                    if (grid[row][col] == 2) {
                        queue.add(new int[]{row, col});
                        visited[row][col] = true;
                    }
                    oranges++;
                }
            }
        }

        if (oranges == 0) return 0;  

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        while (!queue.isEmpty()) {
            int qsize = queue.size();
            days++;

            for (int i = 0; i < qsize; i++) {
                int[] cell = queue.poll();
                oranges--;

                for (int[] dir : directions) {
                    int adjR = cell[0] + dir[0];
                    int adjC = cell[1] + dir[1];

                    if (adjR >= 0 && adjR < R && adjC >= 0 && adjC < C 
                        && grid[adjR][adjC] == 1 && !visited[adjR][adjC]) {
                        grid[adjR][adjC] = 2;
                        visited[adjR][adjC] = true;
                        queue.add(new int[]{adjR, adjC});
                    }
                }
            }
        }

        return oranges > 0 ? -1 : days;
    }
}
