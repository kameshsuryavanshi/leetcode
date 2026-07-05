from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[i][j] will store [max_score, path_count]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: start at the bottom-right corner 'S'
        dp[n-1][n-1] = [0, 1]
        
        # Fill DP table from bottom to top, right to left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in ('X', 'E') and not (i == 0 and j == 0):
                    if board[i][j] == 'X':
                        continue # Obstacle, leave as [-1, 0]
                
                if dp[i][j][0] == -1: 
                    continue # Unreachable cell
                    
                current_score, current_paths = dp[i][j]
                
                # Check three possible movements: up, left, and up-left diagonal
                for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 'X':
                        # Calculate cell value (0 for 'E')
                        cell_val = int(board[ni][nj]) if board[ni][nj] != 'E' else 0
                        next_score = current_score + cell_val
                        
                        # If we found a strictly better score
                        if next_score > dp[ni][nj][0]:
                            dp[ni][nj] = [next_score, current_paths]
                        # If we found an alternative path resulting in the same max score
                        elif next_score == dp[ni][nj][0]:
                            dp[ni][nj][1] = (dp[ni][nj][1] + current_paths) % MOD
        
        # Result is at the top-left corner 'E' (0, 0)
        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]