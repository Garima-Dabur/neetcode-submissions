class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            freq = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in freq:
                        return False
                    freq.add(board[i][j])
        for j in range(len(board)):
            freq = set()
            for i in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in freq:
                        return False
                freq.add(board[i][j])
        for k in range(0, len(board), 3):
            for l in range(0, len(board[0]), 3):
                freq = set()
                for a in range(k, k + 3):
                    for b in range(l, l + 3):
                        if board[a][b] != ".":
                            if board[a][b] in freq:
                                return False 
                            freq.add(board[a][b])
        return True 



                

                
        
        
            


        