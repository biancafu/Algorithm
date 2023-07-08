#17 min
class Solution(object):
    def searchMatrix(self, matrix, target):

        columnlow = 0
        columnhigh = len(matrix) - 1
        rowlength = len(matrix[0])
        column = -1
        while columnlow <= columnhigh:
            columnmid = (columnlow + columnhigh) // 2
            if matrix[columnmid][0] <= target and matrix[columnmid][rowlength - 1] >= target:
                column = columnmid
                break        
            elif matrix[columnmid][0] > target: #if index 0 is greater than target, target will be in rows above
                columnhigh = columnmid - 1
            else: #matrix[columnmid] < target: no and because we excluded the case matrix[columnmid][rowlength - 1] >= target already so matrix[columnmid][rowlength - 1] < target will ahve to be the case
            #if both ends are smaller than target -> target is in lower half
                columnlow = columnmid + 1
        if column == -1:
            return False
                
        low = 0
        high = rowlength - 1
        while low <= high:
            mid = (low + high) // 2
            if target == matrix[columnmid][mid]:
                return True
            elif target > matrix[columnmid][mid]:
                low = mid + 1
            else:
                high = mid - 1