
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        # Brute Force
        m=len(grid)
        n=len(grid[0])
        for _ in range(k):
            last=grid[m-1][n-1]
            for i in range(m*n-1,0,-1):
                r=i//n
                c=i%n
                pr=(i-1)//n
                pc=(i-1)%n
                grid[r][c]=grid[pr][pc]
            grid[0][0]=last

        return grid
        """
         
        m=len(grid)
        n=len(grid[0])
        total=m*n
        k=k%total
        result=[[0]*n for _ in range(m)]
        for i in range(total):
            new=(i+k)%total
            r=new//n
            c=new%n
            result[r][c]=grid[i//n][i%n]
        return result
