class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)] 
        columnSets = [set() for _ in range(9)]
        squareSets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue


                b = (i // 3) * 3 + j // 3

                if val in rowSets[i] or val in columnSets[j] or val in squareSets[b]:
                    return False
                    
                else:
                    rowSets[i].add(val)
                    columnSets[j].add(val)
                    squareSets[b].add(val)

        return True