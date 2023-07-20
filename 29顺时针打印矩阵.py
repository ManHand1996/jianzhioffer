"""
难度:简单
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
 
示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""

def spiralOrder(matrix: list[list[int]]) -> list[int]:
        """
        从外到里
        顺时针: 右,下,左,上
        矩阵边界: top, bottom, left, right
        top:0
        bottom: len(martrix)
        left: 0
        right: len(martrix[0])
        
        打印方向:
        右: 从左到右, (left,right), top += 1, t > b 退出
        下: 从上到下 (top, bottom), right -=1, right < left
        左: 从右往左 (right, left), bottom -= 1, bottom < top
        上: 从下到上 (bottom, top), left += 1, left > right
        """
        if len(matrix) == 0: return []
        res = []
        t, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while True:
            for i in range(l, r+1): res.append(matrix[t][i])
            t += 1
            if t > b:break
            
            for i in range(t, b+1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            
            for i in range(r, l-1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break

            for i in range(b, t-1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res