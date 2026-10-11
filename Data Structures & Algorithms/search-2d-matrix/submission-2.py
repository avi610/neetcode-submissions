class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows,cols,total = len(matrix),len(matrix[0]),len(matrix)*len(matrix[0])
        lo, hi = 0, total-1

        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            col = mid // cols
            row = mid % cols
            if matrix[col][row] == target:
                return True
            elif matrix[col][row] < target:
                lo = mid + 1
            else:
                hi = mid -1
        
        return False