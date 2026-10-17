class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS=len(matrix),len(matrix[0])
        cache={} #以 (r,c) 为左上角，能够构成的最大全 1 正方形的边长

        def dfs(r,c):
            if r>=ROWS or c>=COLS:
                return 0
            if (r,c) not in cache:
                down=dfs(r+1,c)
                right=dfs(r,c+1)
                diag=dfs(r+1,c+1)
                cache[(r,c)]=0
                if matrix[r][c]=='1':
                    cache[(r,c)]=1+min(down,right,diag)
            return cache[(r,c)]
        
        dfs(0,0)
        return max(cache.values())**2