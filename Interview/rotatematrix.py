#https://app.codesignal.com/interview-practice/question/5A8jwLGcEpTPyyjTB/solutions

def solution(a):
    '''
    y
    [0,0] -> [0,2]
    [0,2] -> [2,2]
    [2,2] -> [2,0]
    [2,0] -> [0,0]
    
    [0,1] -> [1,2]
    [1,2] -> [2,1]
    [2,1] -> [1,0]
    
    [0][0,1,2] -> [0,1,2][2]
    [2][0,1,2] -> [0,1,2][0]
    
    read it vertical from bottom up, left to right
    '''
    n = len(a)
    b = [[0]*(n) for i in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n):
            b[j][n-1-i] = a[i][j]
    
    return b
            

#someone's solution
#easier to reverse then transpose
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
#            reverse     swap
def solution2(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


#anti clockwise rotate (-90 rotate)
def antilcockwise(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()
    return matrix


solution2([[1,2,3],
           [4,5,6],
           [7,8,9]])

a = antilcockwise([ [1,2,3],
                    [4,5,6],
                    [7,8,9]])

# 3 6 9
# 2 5 8 
# 1 4 7

print(a)