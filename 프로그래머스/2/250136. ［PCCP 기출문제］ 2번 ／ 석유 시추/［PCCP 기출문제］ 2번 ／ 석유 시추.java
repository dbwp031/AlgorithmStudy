import java.util.*;

class Solution {
    private static final int[] DR = {1, 0, -1, 0};
    private static final int[] DC = {0, 1, 0, -1};

    public int solution(int[][] land) {
        int rows = land.length;
        int columns = land[0].length;

        boolean[][] visited = new boolean[rows][columns];
        int[] oilByColumn = new int[columns];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < columns; c++) {
                if (land[r][c] == 0 || visited[r][c]) {
                    continue;
                }

                Set<Integer> touchedColumns = new HashSet<>();

                int oilSize = bfs(
                    land,
                    visited,
                    r,
                    c,
                    rows,
                    columns,
                    touchedColumns
                );

                for (int column : touchedColumns) {
                    oilByColumn[column] += oilSize;
                }
            }
        }

        int answer = 0;

        for (int oil : oilByColumn) {
            answer = Math.max(answer, oil);
        }

        return answer;
    }

    private int bfs(
        int[][] land,
        boolean[][] visited,
        int startRow,
        int startColumn,
        int rows,
        int columns,
        Set<Integer> touchedColumns
    ) {
        Queue<Integer> queue = new ArrayDeque<>();

        queue.offer(startRow * columns + startColumn);
        visited[startRow][startColumn] = true;

        int oilSize = 0;

        while (!queue.isEmpty()) {
            int position = queue.poll();
            int row = position / columns;
            int column = position % columns;

            oilSize++;
            touchedColumns.add(column);

            for (int direction = 0; direction < 4; direction++) {
                int nextRow = row + DR[direction];
                int nextColumn = column + DC[direction];

                if (
                    nextRow < 0 || nextRow >= rows ||
                    nextColumn < 0 || nextColumn >= columns
                ) {
                    continue;
                }

                if (
                    visited[nextRow][nextColumn] ||
                    land[nextRow][nextColumn] == 0
                ) {
                    continue;
                }

                visited[nextRow][nextColumn] = true;
                queue.offer(nextRow * columns + nextColumn);
            }
        }

        return oilSize;
    }
}