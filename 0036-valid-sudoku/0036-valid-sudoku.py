class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        column=defaultdict(set)
        grid=defaultdict(set)
        for i,rows in enumerate(board):
            for j,num in enumerate(rows):
                if num=='.':
                    continue
                if (num in row[i] or num in column[j] or num in grid[(i//3,j//3)]):
                    return False
                
                row[i].add(num)
                column[j].add(num)
                grid[(i//3,j//3)].add(num)
        return True