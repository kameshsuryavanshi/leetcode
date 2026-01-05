class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rs = set()
        cs = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rs.add(i)
                    cs.add(j)
        
        # print(rs,cs)/
        for i in rs:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in cs:
            for i in range (len(matrix)):
                matrix[i][j] = 0

        # # Validate input
        # if not matrix or not isinstance(matrix, list):
        #     return

        # m = len(matrix)
        # n = len(matrix) if m > 0 else 0
        
        # # Check if first row and first column have zeros
        # first_row_has_zero = False
        # first_col_has_zero = False
        
        # for j in range(n):
        #     if matrix[j] == 0:
        #         first_row_has_zero = True
        #         break
        
        # for i in range(m):
        #     if matrix[i] == 0:
        #         first_col_has_zero = True
        #         break
        
        # # Use first row and column as flags
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] == 0:
        #             matrix[j] = 0
        #             matrix[i] = 0
        
        # # Set zeros based on flags
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[j] == 0 or matrix[i] == 0:
        #             matrix[i][j] = 0
        
        # # Set first row to zero if needed
        # if first_row_has_zero:
        #     for j in range(n):
        #         matrix[j] = 0
        
        # # Set first column to zero if needed
        # if first_col_has_zero:
        #     for i in range(m):
        #         matrix[i] = 0