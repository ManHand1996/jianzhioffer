"""
在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，
每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

答案:https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solutions/95306/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
"""
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1.遍历矩阵所有元素(O(m*n))
        # 2.对每行进行二分法搜索 (O(m*logn))
        # i = 0
        # while i < len(matrix):
        #     row = matrix[i]
        #     while row:
        #         mid_idx = len(row)/2
        #         if row[mid_idx] == target:
        #             return True
        #         elif row[mid_idx] < target:
        #             row = row[mid_idx:]
        #         else:
        #             row = row[:mid_idx]
        #         if mid_idx == 0:
        #             break
            
        #     i +=1
        # return False

        # 3.逐渐减少搜索的矩阵大小 O(m+n) safs
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False