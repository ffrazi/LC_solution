import java.util.*;

class Orange {
    int row, col, days;
    public Orange(int r, int c, int d) {
        this.row = r;
        this.col = c;
        this.days = d;
    }
}

class Solution {
    public int orangesRotting(int[][] grid) {
        int R = grid.length, C = grid[0].length;
        boolean[][] visited = new boolean[R][C];
        Queue<Orange> queue = new LinkedList<>();
        int days = 0, oranges = 0;

        for (int row = 0; row < R; row++) {
            for (int col = 0; col < C; col++) {
                if (grid[row][col] != 0) {
                    if (grid[row][col] == 2) {
                        queue.add(new Orange(row, col, 0));
                        visited[row][col] = true;
                    }
                    oranges++;
                }
            }
        }

        if (oranges == 0) return 0;  

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        while (!queue.isEmpty()) {
            Orange rotten = queue.poll();
            oranges--;
            days = Math.max(days, rotten.days);

            for (int index = 0; index < 4; index++) {
                int adjR = rotten.row + directions[index][0];
                int adjC = rotten.col + directions[index][1];

                if (adjR >= 0 && adjR < R && adjC >= 0 && adjC < C) {
                    if (grid[adjR][adjC] == 1 && !visited[adjR][adjC]) {
                        queue.add(new Orange(adjR, adjC, rotten.days + 1));
                        visited[adjR][adjC] = true;
                        grid[adjR][adjC] = 2;  
                    }
                }
            }
        }

        return oranges > 0 ? -1 : days;
    }
}