"""Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    result = []
    if not matrix:
        return result
    
    top = 0 # starting row
    bottom = len(matrix)-1 #ending row
    left = 0 #stating coloumn
    right = len(matrix[0]) -1 #ending column
    while top<=bottom and left <=right:
        #1 Left ->right
        for col in range(left,right+1):
            result.append(matrix[top][col])
        top+=1
        
        #top -> bottom
        for row in range(top,bottom+1):
            result.append(matrix[row][right])
        right -=1
        
        #right -> left 
        if top <=bottom:
            for col in range(right,left-1,-1):
                result.append(matrix[bottom][col])
            bottom -=1
        
        if left <= right:
            for row in range(bottom,top-1,-1):
                result.append(matrix[row][left])
            left+=1
    
    return result
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
                
        
        
    
