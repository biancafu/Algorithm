#17 min O(logmn) (same logic as neetcode)
def searchMatrix_neetcode(self, matrix, target):
        rleft = 0
        rright = len(matrix) - 1
        mid = -1
        while rleft <= rright:
            rmid = (rleft + rright) // 2
            if matrix[rmid][-1] < target:
                rleft = rmid + 1
                #last number < target, then it must be somewhere below this row since it is greater than the largest num in row
            elif matrix[rmid][0] > target:
                #if first number is still greater than target, means target must be above since smallest number of the row is greater than target
                rright = rmid - 1
            else: #when it fits in the row
                mid = rmid
                break
        
        if mid == -1:
            return False

        l = 0
        h = len(matrix[0]) - 1
        while l <= h:
            m = (l + h) // 2
            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                h = m - 1
            else:
                return True
        return False
        
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

    #this solutioin can be faster depending on the test case but ultimately, it is O(n^2) time complexity
    #since if r is in last row, that means we have to go m times and if column is last, we have to go mxn times
    def searchMatrix_other (self, matrix,target):
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target: r += 1
            elif matrix[r][c] > target: c -= 1
            else: return True
        
        return False